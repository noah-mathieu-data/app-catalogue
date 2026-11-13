import streamlit as st
import pandas as pd

FICHIER = "data/livres_poetry.csv"

st.set_page_config(page_title="Catalogue Poetry", page_icon="📚", layout="wide")


@st.cache_data
def charger_donnees(chemin):
    return pd.read_csv(chemin)


df = charger_donnees(FICHIER)

st.title("📚 Explorateur du catalogue Poetry")
st.caption("19 livres collectés sur books.toscrape.com · filtre-les avec le menu de gauche")

with st.sidebar:
    st.header("🔎 Filtres")

    note_mini = st.slider("Note minimale", 1, 5, 1)

    prix_min, prix_max = st.slider(
        "Fourchette de prix (GBP)",
        float(df["prix_gbp"].min()),
        float(df["prix_gbp"].max()),
        (float(df["prix_gbp"].min()), float(df["prix_gbp"].max())),
    )

    recherche = st.text_input("Le titre contient")

selection = df.copy()
selection = selection[selection["note"] >= note_mini]
selection = selection[(selection["prix_gbp"] >= prix_min) & (selection["prix_gbp"] <= prix_max)]

if recherche:
    selection = selection[selection["titre"].str.contains(recherche, case=False)]

if len(selection) == 0:
    st.warning("Aucun livre ne correspond à ces critères.")
    st.stop()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Livres retenus", f"{len(selection)} / {len(df)}")
col2.metric("Prix moyen", f"{selection['prix_gbp'].mean():.2f} GBP")
col3.metric("Note moyenne", f"{selection['note'].mean():.2f} / 5")
col4.metric("Stock total", f"{selection['stock'].sum()} ex.")

st.divider()

st.subheader("Les livres retenus")
st.dataframe(selection, hide_index=True, width="stretch")

gauche, droite = st.columns(2)

with gauche:
    st.subheader("Les 5 mieux notés")
    st.dataframe(selection.nlargest(5, "note")[["titre", "note"]], hide_index=True)

with droite:
    st.subheader("Les 5 moins chers")
    st.dataframe(selection.nsmallest(5, "prix_gbp")[["titre", "prix_gbp"]], hide_index=True)

with st.expander("Voir le catalogue complet sans filtre associé"):
    st.dataframe(df, hide_index=True)