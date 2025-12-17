import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier, export_text
from matplotlib.colors import ListedColormap

# --- Inställningar och titlar ---
st.set_page_config(layout="wide")
st.title("Rule-Extraction Playground (Uppgift 04)")
st.caption("Utforska Global Regelutvinning: Decision-Tree Surrogate")
st.markdown("---")

# --- Sidebar för GenAI Litteracitet ---
st.sidebar.markdown("## GenAI Litteracitet")
st.sidebar.info("Hela uppgiften, inklusive denna kod och presentation, har utformats med hjälp av en stor språkmodell (Gemini).")

# --- 1. Datagenerering och Kontroller ---
st.subheader("1. Toy Dataset (Leksaksdata) & Inställningar")
col1, col2 = st.columns([1, 2]) # För att placera grafer och reglage snyggt

with col1:
    st.markdown("### Data Kontroller")
    n_samples = st.slider("Antal datapunkter", 50, 1000, 500)
    noise = st.slider("Brus (Noise)", 0.01, 0.50, 0.1, step=0.01)

# Generera data
X, y_true = make_moons(n_samples=n_samples, noise=noise, random_state=42)

# --- 2. Basmodell (Den Svarta Lådan) ---
# Träna en komplex modell (MLP)
mlp_model = MLPClassifier(
    solver='lbfgs',
    alpha=1e-5,
    hidden_layer_sizes=(10, 10),
    random_state=1
)
mlp_model.fit(X, y_true)
y_mlp_pred = mlp_model.predict(X) # MLP:s förutsägelser blir våra pseudo-etiketter

# --- 3. Surrogatmodell (Regelutvinning) ---
st.subheader("2. Decision-tree surrogate (global)")
max_depth = st.slider("Max depth (Maximalt djup på Beslutsträdet)", 1, 8, 3)

# Träna surrogatmodellen på MLP:s pseudo-etiketter
surrogate_tree = DecisionTreeClassifier(max_depth=max_depth, random_state=42)
surrogate_tree.fit(X, y_mlp_pred) # Tränas på den svarta lådans utdata

# Extrahera regler
feature_names = ["X1", "X2"]
rules_text = export_text(
    surrogate_tree,
    feature_names=feature_names,
    decimals=3
)

# Beräkna trohet (fidelity)
y_tree_pred = surrogate_tree.predict(X)
fidelity = np.mean(y_tree_pred == y_mlp_pred) * 100

st.metric(label="Trohet (Fidelity) till Svart Låda", value=f"{fidelity:.2f}%")
st.caption(f"Trädets komplexitet: {surrogate_tree.tree_.node_count} noder.")

st.markdown("#### Extraherade IF-THEN Regler (Global Förklaring):")
st.code(rules_text, language='text')

st.markdown("---")

# --- 4. Visualisering (Grafer) ---
# Skapa en meshgrid för plottning av beslutsgränser
h = .02
x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))

fig, ax = plt.subplots(1, 2, figsize=(12, 5))
cm = plt.cm.RdBu
cm_bright = ListedColormap(['#FF0000', '#0000FF'])

# --- Plot 1: Basmodell (MLP) ---
Z_mlp = mlp_model.predict_proba(np.c_[xx.ravel(), yy.ravel()])[:, 1]
Z_mlp = Z_mlp.reshape(xx.shape)
ax[0].contourf(xx, yy, Z_mlp, cmap=cm, alpha=.8)
ax[0].scatter(X[:, 0], X[:, 1], c=y_true, cmap=cm_bright, edgecolors='k')
ax[0].set_title(f"Svart Låda (MLP) - Beslutsgräns")
ax[0].set_xticks(())
ax[0].set_yticks(())

# --- Plot 2: Surrogat (Beslutsträd) ---
Z_tree = surrogate_tree.predict_proba(np.c_[xx.ravel(), yy.ravel()])[:, 1]
Z_tree = Z_tree.reshape(xx.shape)
ax[1].contourf(xx, yy, Z_tree, cmap=cm, alpha=.8)
ax[1].scatter(X[:, 0], X[:, 1], c=y_mlp_pred, cmap=cm_bright, edgecolors='k')
ax[1].set_title(f"Decision-Tree Surrogate (Regler)")
ax[1].set_xticks(())
ax[1].set_yticks(())

st.pyplot(fig)
st.caption("Jämför beslutsgränserna: Den högra grafen visar hur de extraherade reglerna (surrogatmodellen) förenklar den komplexa logiken från MLP-modellen (vänster).")

# --- 5. Greedy Rule Miner (Platshållare för presentationen) ---
st.subheader("3. Greedy Rule Miner (Global Decision Set) - Konceptuell platshållare")
st.markdown("*I en komplett demo skulle detta avsnitt visa en uppsättning regler optimerade för maximal täckning och precision, istället för att bara approximera hela modellen.*")
if st.button("Visa Exempel på Högprecisionsregel"):
    st.info("OM X1 > 1.2 OCH X2 < 0.5 DÅ KLASS = RÖD")