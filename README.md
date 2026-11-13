# Learning Streamlit

Streamlit turns a Python script into an interactive web app, so you can share a dataset or a model without writing any HTML, CSS or JavaScript. This repository is the scaffold for a live-coding session: you build a multipage Pokémon app step by step alongside your coach, starting from an empty `app.py`. The dataset and a trained classifier are provided, so the session stays focused on Streamlit itself.

## Learning Objectives

By the end of this repository, you should be able to:

- Run a Streamlit app locally and use its automatic reload while you edit the script.
- Build a page from Streamlit commands that display text, dataframes and charts.
- Collect user input with widgets (sliders, select boxes, buttons) and react to it.
- Split an app into multiple pages and share data between them with `st.session_state`.
- Cache expensive work with `st.cache_data` and `st.cache_resource` to keep the app responsive.
- Serve predictions from a trained model in response to user input.

## Learning Path

Skim the essentials, train the model in the notebook, then build the app during the session:

| File / Folder                                              | Description                                                                                        |
| ---------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| [**Streamlit Essentials**](streamlit_essentials.md)        | Reference notes on the rerun model, widgets, layout, caching and multipage apps.                    |
| [**EDA and Modeling**](EDA_and_modeling.ipynb)             | Explore the Pokémon dataset, then train and save the Random Forest classifier the app will use.     |
| [**app.py**](app.py)                                       | Entry point of the app. Empty on purpose: you write the page configuration and navigation live.     |
| [**Pages**](pages/)                                        | One script per page of the app. You add these during the session.                                   |
| [**predict.py**](predict.py)                               | Provided helper that loads the saved model and returns a prediction plus its probability.           |

### Additional Folders and Files

| File / Folder                        | Description                                                                        |
| ------------------------------------ | ---------------------------------------------------------------------------------- |
| [**Data**](data/)                    | `pokemon.csv`, 801 Pokémon with battle stats, type, size, coordinates and legendary flag. |
| [**Models**](models/)                | Destination for the classifier saved by the notebook. The `.pkl` file is not tracked in git.   |
| [**Images**](images/)                | Image assets available to the app.                                                 |
| [**Solutions**](solutions/)          | Reference implementation of the finished app.                                       |
| [**pyproject.toml**](pyproject.toml) | Project configuration and dependencies.                                             |
| [**uv.lock**](uv.lock)               | Dependency lock file.                                                              |

## Setup

> [!NOTE]
> Throughout these steps, text in angle brackets like `<repo-name>` is a **placeholder**. Replace it including the `< >` brackets with your own value. For example, `cd <repo-name>` becomes `cd learning-streamlit`.

### 1. Create the Repository from the Template

Click **Use this template** on GitHub.

When creating the repository:

- Set yourself as the **Owner**
- Choose a repository name
- Disable **Include all branches**
- Click **Create repository**

---

### 2. Clone the Repository

Copy the SSH URL from the **Code** button on GitHub, then run:

```bash
git clone <copied-ssh-url>
```

The copied SSH URL will look like `git@github.com:<your-username>/<repo-name>.git`.

---

### 3. Move into the Project Folder and Install Dependencies

This installs all dependencies and creates a virtual environment in `.venv/`.

```bash
cd <repo-name>
uv sync
```

---

### 4. Train the Model

Launch VS Code in the project root folder:

```bash
code .
```

Open `EDA_and_modeling.ipynb`, select the Python environment created by `uv sync` as the kernel, and run all cells. The last cell writes `models/random_forest.pkl`.

> [!IMPORTANT]
> Run the notebook before the prediction page of the app. Without `models/random_forest.pkl`, `predict.py` cannot load the model.

---

### 5. Run the App

```bash
uv run streamlit run app.py
```

The app opens in your browser at `http://localhost:8501`. Leave this command running while you code: Streamlit reloads the app every time you save a file.

> [!TIP]
> Arrange your editor and the browser side by side. You then see each change take effect as soon as you save.

`app.py` is empty at the start of the session, so the first run shows a blank page. That is expected.

## References & Further Reading

- [**Streamlit Essentials**](streamlit_essentials.md): The reference notes for this session, in one page
- [**Streamlit main concepts**](https://docs.streamlit.io/get-started/fundamentals/main-concepts): How a Streamlit script becomes an app, and how the rerun model works
- [**Streamlit API reference**](https://docs.streamlit.io/develop/api-reference): Every command, grouped by what it does
- [**Multipage apps**](https://docs.streamlit.io/develop/concepts/multipage-apps): Navigation with `st.navigation` and the `pages/` folder
- [**Caching**](https://docs.streamlit.io/develop/concepts/architecture/caching): When to reach for `st.cache_data` and when for `st.cache_resource`
- [**Session state**](https://docs.streamlit.io/develop/concepts/architecture/session-state): Keeping values across reruns and sharing them between pages
- [**Plotly Express**](https://plotly.com/python/plotly-express/): The charting library used for the interactive figures in this app
- [**Streamlit gallery**](https://streamlit.io/gallery): Apps built by the community, useful for seeing what is possible
- [**uv documentation**](https://docs.astral.sh/uv/): The package manager used in this repository

Other Python web frameworks, if you want to compare approaches:

- [**Dash**](https://dash.plotly.com): Dashboards built on Plotly and Flask
- [**Django**](https://www.djangoproject.com): Full-stack framework for larger web applications
- [**Flask**](https://flask.palletsprojects.com/en/stable/): Minimal backend framework
- [**FastAPI**](https://fastapi.tiangolo.com): Backend framework focused on APIs
- [**Taipy**](https://docs.taipy.io): Data and AI apps with a separate core and GUI layer

## License

[MIT license](LICENSE)
