CREATE CONSTRAINT UniqueKanji ON (k:Kanji) ASSERT k.value IS UNIQUE;
CREATE CONSTRAINT UniqueMeaning ON (m:Meaning) ASSERT m.value IS UNIQUE;
CREATE CONSTRAINT UniqueRadical ON (r:Radical) ASSERT r.value IS UNIQUE;
CREATE CONSTRAINT UniqueTheme ON (t:Theme) ASSERT t.value IS UNIQUE;
CREATE CONSTRAINT UniqueSubtheme ON (st:Subtheme) ASSERT st.value IS UNIQUE;
