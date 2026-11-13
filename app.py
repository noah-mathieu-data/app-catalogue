import streamlit as st
import pandas as pd

FICHIER = "data/livres_poetry.csv"

st.set_page_config(page_title="Le rayon Poésie", page_icon="🪶", layout="wide")


st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,700;1,500&display=swap');

/* le fond : des étagères pleines de livres, assombries pour garder le texte lisible */
[data-testid="stAppViewContainer"] {
    background:
        linear-gradient(rgba(20, 12, 6, 0.70), rgba(20, 12, 6, 0.82)),
        repeating-linear-gradient(to bottom, transparent 0px, transparent 150px, #4A2C16 150px, #2E1A0C 170px),
        repeating-linear-gradient(to right,
            #6B1F1A 0px, #6B1F1A 16px,
            #2F3D27 16px, #2F3D27 28px,
            #7A5320 28px, #7A5320 46px,
            #1F2C3D 46px, #1F2C3D 56px,
            #5A2A14 56px, #5A2A14 74px,
            #3A2A1A 74px, #3A2A1A 80px,
            #4B1D2E 80px, #4B1D2E 96px,
            #6E5A2B 96px, #6E5A2B 108px);
}

/* la lueur du feu, qui vacille doucement en bas de l'écran */
[data-testid="stAppViewContainer"]::before {
    content: "";
    position: fixed;
    inset: 0;
    background: radial-gradient(ellipse at 50% 115%, rgba(255, 120, 30, 0.40) 0%, rgba(255, 90, 20, 0.12) 35%, transparent 65%);
    animation: feu 2.5s ease-in-out infinite alternate;
    pointer-events: none;
    z-index: 0;
}
@keyframes feu {
    0%   { opacity: 0.65; }
    40%  { opacity: 0.95; }
    70%  { opacity: 0.75; }
    100% { opacity: 1; }
}

[data-testid="stHeader"] { background: transparent; }

[data-testid="stMainBlockContainer"], .block-container {
    position: relative;
    z-index: 1;
}

/* la barre de gauche en bois */
[data-testid="stSidebar"] {
    background: repeating-linear-gradient(90deg, #3B2414 0px, #45291A 3px, #3B2414 7px, #33200F 11px);
    border-right: 2px solid #8B5A2B;
}

h1, h2, h3, .titre-or {
    font-family: 'Cormorant Garamond', serif !important;
}

/* la bannière d'accueil */
.banniere {
    text-align: center;
    padding: 3rem 1rem 2.5rem 1rem;
    border-radius: 18px;
    background: radial-gradient(circle at top, rgba(74, 44, 22, 0.95) 0%, rgba(28, 18, 11, 0.95) 75%);
    border: 1px solid rgba(217, 163, 91, 0.45);
    box-shadow: 0 0 40px rgba(255, 120, 30, 0.15);
    margin-bottom: 2rem;
}
.banniere .titre-or {
    font-size: 4rem;
    font-weight: 700;
    color: #D9A35B;
    margin: 0;
    letter-spacing: 2px;
    text-shadow: 0 0 18px rgba(255, 140, 40, 0.45);
}
.banniere .sous-titre {
    font-size: 1.1rem;
    color: #C9B391;
    margin-top: 0.3rem;
    letter-spacing: 4px;
    text-transform: uppercase;
}
.banniere .citation {
    font-family: 'Cormorant Garamond', serif;
    font-style: italic;
    font-size: 1.5rem;
    color: #F1E4CC;
    margin-top: 1.8rem;
}
.banniere .auteur {
    color: #D9A35B;
    font-size: 0.95rem;
    margin-top: 0.4rem;
}

/* les 4 chiffres, en cartes de bois */
[data-testid="stMetric"] {
    background: rgba(43, 28, 18, 0.92);
    border: 1px solid #8B5A2B;
    border-radius: 14px;
    padding: 1rem 1.2rem;
    box-shadow: 0 4px 18px rgba(0, 0, 0, 0.45);
}
[data-testid="stMetricValue"] {
    color: #D9A35B;
    font-family: 'Cormorant Garamond', serif;
    font-size: 2.3rem !important;
}

/* le recueil à la une */
.carte-une {
    background: linear-gradient(135deg, rgba(74, 44, 22, 0.95) 0%, rgba(43, 28, 18, 0.95) 100%);
    border-left: 5px solid #D9A35B;
    border-radius: 14px;
    padding: 1.5rem 2rem;
    margin: 1.5rem 0;
    box-shadow: 0 4px 18px rgba(0, 0, 0, 0.45);
}
.carte-une .etiquette {
    color: #D9A35B;
    letter-spacing: 3px;
    text-transform: uppercase;
    font-size: 0.8rem;
}
.carte-une .nom-livre {
    font-family: 'Cormorant Garamond', serif;
    font-size: 2rem;
    font-weight: 700;
    color: #F1E4CC;
    margin: 0.3rem 0;
}
.carte-une .details {
    color: #C9B391;
    font-size: 1.05rem;
}

/* les tableaux et les onglets sur un fond de bois sombre */
[data-testid="stDataFrame"], [data-testid="stTabs"], [data-testid="stExpander"] {
    background: rgba(28, 18, 11, 0.9);
    border-radius: 12px;
    padding: 0.5rem;
}
</style>
""", unsafe_allow_html=True)

@st.cache_data
def charger_donnees(chemin):
    return pd.read_csv(chemin)


df = charger_donnees(FICHIER)
df["etoiles"] = df["note"].apply(lambda n: "★" * n + "☆" * (5 - n))


st.markdown("""
<div class="banniere">
<p class="titre-or">🕯️ Le rayon Poésie</p>
<p class="sous-titre">19 recueils · books.toscrape.com</p>
<p class="citation">« Les parfums, les couleurs et les sons se répondent. »</p>
<p class="auteur">Charles Baudelaire · Correspondances, 1857</p>
</div>
""", unsafe_allow_html=True)


with st.sidebar:
    st.header("🪶 Filtres")
    st.caption("Tout se met à jour dès que tu bouges un réglage.")

    note_mini = st.slider("Note minimale", 1, 5, 1)

    prix_min, prix_max = st.slider(
        "Fourchette de prix (GBP)",
        float(df["prix_gbp"].min()),
        float(df["prix_gbp"].max()),
        (float(df["prix_gbp"].min()), float(df["prix_gbp"].max())),
    )

    recherche = st.text_input("Le titre contient", placeholder="ex. poems")

    st.divider()
    st.caption("Projet Wild Code School · Noah Mathieu")


selection = df.copy()
selection = selection[selection["note"] >= note_mini]
selection = selection[(selection["prix_gbp"] >= prix_min) & (selection["prix_gbp"] <= prix_max)]

if recherche:
    selection = selection[selection["titre"].str.contains(recherche, case=False)]


if len(selection) == 0:
    st.warning("Aucun recueil ne correspond à ces critères. Élargis les filtres à gauche.")
    st.stop()


filtre_actif = len(selection) < len(df)

prix_moyen = selection["prix_gbp"].mean()
note_moyenne = selection["note"].mean()
stock = selection["stock"].sum()

col1, col2, col3, col4 = st.columns(4)
col1.metric("📖 Recueils", f"{len(selection)} / {len(df)}")
col2.metric(
    "💷 Prix moyen",
    f"{prix_moyen:.2f} £",
    delta=f"{prix_moyen - df['prix_gbp'].mean():+.2f} vs catalogue" if filtre_actif else None,
    delta_color="inverse",
)
col3.metric(
    "⭐ Note moyenne",
    f"{note_moyenne:.2f} / 5",
    delta=f"{note_moyenne - df['note'].mean():+.2f} vs catalogue" if filtre_actif else None,
)
col4.metric(
    "📦 Stock",
    f"{stock} ex.",
    delta=f"{stock / df['stock'].sum():.0%} du stock total" if filtre_actif else None,
    delta_color="off",
)


une = selection.sort_values(["note", "stock"], ascending=False).iloc[0]

st.markdown(f"""
<div class="carte-une">
<div class="etiquette">✦ Le recueil à la une</div>
<div class="nom-livre">{une['titre']}</div>
<div class="details">{une['etoiles']} &nbsp;·&nbsp; {une['prix_gbp']:.2f} £ &nbsp;·&nbsp; {une['stock']} exemplaires en stock</div>
</div>
""", unsafe_allow_html=True)


onglet1, onglet2, onglet3 = st.tabs(["📜 Catalogue", "🏆 Palmarès", "📊 Statistiques"])

colonnes = {
    "titre": st.column_config.TextColumn("Titre", width="large"),
    "etoiles": st.column_config.TextColumn("Note"),
    "prix_gbp": st.column_config.NumberColumn("Prix", format="%.2f £"),
    "stock": st.column_config.ProgressColumn(
        "Stock", min_value=0, max_value=int(df["stock"].max()), format="%d ex."
    ),
}

with onglet1:
    st.dataframe(
        selection[["titre", "etoiles", "prix_gbp", "stock"]],
        column_config=colonnes,
        hide_index=True,
        width="stretch",
    )

with onglet2:
    gauche, droite = st.columns(2)

    with gauche:
        st.subheader("Les 5 mieux notés")
        st.dataframe(
            selection.nlargest(5, "note")[["titre", "etoiles"]],
            column_config=colonnes,
            hide_index=True,
            width="stretch",
        )

    with droite:
        st.subheader("Les 5 moins chers")
        st.dataframe(
            selection.nsmallest(5, "prix_gbp")[["titre", "prix_gbp"]],
            column_config=colonnes,
            hide_index=True,
            width="stretch",
        )

with onglet3:
    gauche, droite = st.columns(2)

    with gauche:
        st.subheader("Combien de recueils par note")
        repartition = selection["note"].value_counts().sort_index()
        st.bar_chart(repartition, color="#D9A35B")

    with droite:
        st.subheader("Les chiffres clés")
        stats = selection[["prix_gbp", "note", "stock"]].describe().round(2)
        st.dataframe(stats, width="stretch")


with st.expander("Voir le catalogue complet, sans filtre"):
    st.dataframe(df.drop(columns="etoiles"), hide_index=True, width="stretch")

st.caption("« La poésie est le miroir brouillé de la société. » · Louis Aragon")