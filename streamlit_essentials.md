# Streamlit Essentials

Reference notes for the live-coding session. Skim them before you start, then come back to them while you build the app. Based on the [Streamlit documentation](https://docs.streamlit.io/get-started/fundamentals/main-concepts).

Streamlit is a Python library for building interactive web apps for data science and machine learning. You write an ordinary Python script, add Streamlit commands to it, and run it with `streamlit run app.py`.

## App Model

- A Streamlit app is a Python script that executes from top to bottom.
- Streamlit reruns the entire script whenever you save the file or a user interacts with a widget.
- Everything you see in the browser is produced by that run, so there is no callback or event system to learn.

Almost every pattern below follows from this one fact.

## Development Flow

- Write code, save, look at the result, repeat. The app reloads on save.
- Keep the command running while you work: `uv run streamlit run app.py`.
- Arrange your editor and the browser side by side so you see each change immediately.

## Data Flow

- A rerun re-executes every line, including the expensive ones, unless you prevent it.
- Widgets return their current value on each rerun, so you read them like ordinary variables.
- Values that must survive a rerun, or be shared between pages, belong in `st.session_state`.

## Displaying Data

- `st.write` accepts almost anything: text, Markdown, a dataframe, a chart.
- `st.dataframe` renders an interactive table, `st.table` a static one.
- `st.plotly_chart` renders a Plotly figure. `st.map` draws points from latitude and longitude columns with no configuration at all.

## Widgets

Widgets collect user input. Each one returns its value directly:

```python
weight = st.slider('Select weight', min_value=0, max_value=1000, step=5)
model = st.selectbox('Select a model', ['LogReg', 'Random Forest', 'XGBoost'])
if st.button('Press me'):
    st.write('Pressed')
```

- `st.number_input` and `st.slider` enforce their own range. `st.text_input` returns a string and enforces nothing, so you have to parse and clamp the value yourself.
- Put work you do not want repeated on every keystroke behind `st.button`.

## Layout

- `st.sidebar` moves any element into the sidebar.
- `st.columns` places elements side by side.
- `st.tabs` separates alternative views of the same thing.
- `st.expander` hides detail until the reader asks for it.

## Caching

Two decorators, chosen by what you are storing:

- `@st.cache_data` for computations that return data, such as loading a CSV or aggregating a dataframe. Each caller gets its own copy.
- `@st.cache_resource` for global objects that should exist once and be shared, such as a trained model or a database connection.

Reaching for `cache_data` on a model would copy it per session, which is why `predict.py` uses `cache_resource`.

## Multipage Apps

- Put one script per page in a `pages/` folder.
- Declare the pages with `st.Page` and build the navigation with `st.navigation` in your entry point, which gives you control over titles, icons and order.
- Pages do not share variables. Anything a page needs from the entry point goes through `st.session_state`, which also means a page that reads `st.session_state` cannot be run on its own.

## Progress and Themes

- `st.progress` and `st.spinner` show that a long computation is running.
- `st.success`, `st.error` and `st.warning` report an outcome.
- Light and dark themes are available from the app menu, and can be set in `.streamlit/config.toml`.

## Further Reading

- [Streamlit API reference](https://docs.streamlit.io/develop/api-reference): every command, grouped by what it does
- [Multipage apps](https://docs.streamlit.io/develop/concepts/multipage-apps): navigation patterns in detail
- [Caching](https://docs.streamlit.io/develop/concepts/architecture/caching): the full rules, including hashing and TTLs
- [Session state](https://docs.streamlit.io/develop/concepts/architecture/session-state): keeping values across reruns
