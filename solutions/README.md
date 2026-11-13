# Solutions

Reference implementation of the multipage Pokémon app built during the live-coding session. Open any file alongside your own version to compare approaches.

Run it from the repository root, so the `data/` and `images/` paths resolve:

```bash
uv run streamlit run solutions/app.py
```

> [!IMPORTANT]
> Run `EDA_and_modeling.ipynb` first. The prediction page needs `models/random_forest.pkl`, which the notebook creates.

| File / Folder                                 | Description                                                                                            |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| [**app.py**](app.py)                          | Entry point: page configuration, the dataset loaded once into `st.session_state`, and `st.navigation`.  |
| [**Welcome**](pages/home.py)                  | Text, Markdown and an image, plus the HTML alternative to `st.title` shown as a comment.                |
| [**EDA**](pages/eda.py)                       | Checkbox-gated dataframe, a Plotly Express scatter plot, and a radar chart built with `graph_objects`.  |
| [**Prediction**](pages/prediction.py)         | Three input styles side by side in columns, then a prediction from the trained model behind a button.   |
| [**Map viz**](pages/map.py)                   | Two tabs comparing built-in `st.map` against a configurable Plotly `scatter_geo`.                       |
| [**Pokédex**](pages/pokedex.py)               | Chat interface where the history is replayed from `st.session_state` on every rerun.                    |
| [**predict.py**](predict.py)                  | Copy of the provided helper, so imports resolve when `solutions/app.py` is the entry point.             |

For the concepts behind the code, see [Streamlit Essentials](../streamlit_essentials.md).
