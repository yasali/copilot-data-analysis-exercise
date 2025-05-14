# GitHub Copilot Workshop Guide

## 1. Introduction (Approx. 5 minutes)

This guide outlines how to use GitHub Copilot effectively for the "Finnish Happiness Factor Finder" project (or a similar data-focused project). The aim is to use Copilot for planning, documentation-driven development, and implementation within a timed workshop (e.g., 2 hours). The focus is on structured collaboration with AI.

## 2. Phase 1: Ideation & Planning with Copilot (Approx. 30-40 minutes)

This phase is crucial for setting a clear direction. Effective planning and documentation here will significantly streamline the implementation phase with Copilot.

### 2.1. Review Project Requirements
Refer to the main project description document (e.g., `README.md`) for the "Finnish Happiness Factor Finder" to understand the project's goals and business requirements. Ensure every team member has a clear grasp of the MVP.

### 2.2. Planning Approach with Copilot
Use Copilot Chat for this phase to brainstorm and refine your project's direction.
* **Option A (AI-Led Brainstorming):** If your team is unsure where to start.
    * **Example Prompt (Copilot Chat):**
        ```
        Review the main project description document (e.g., `README.md`) for the 'Finnish Happiness Factor Finder' project. Given these requirements, pre-downloaded data, and potential for PxWeb API fetching:
        1. Propose 2 distinct application architectures (e.g., a collection of scripts for batch processing, a command-line interface (CLI) tool, a web application with a dashboard).
        2. For each architecture, suggest suitable primary programming languages and relevant key frameworks/libraries for data analysis and visualization.
        3. Outline main components for each.
        Focus on MVP achievable in 2 hours.
        ```
* **Option B (Participant-Led, AI-Refined):** If your team has initial ideas.
    * **Example Prompt (Copilot Chat):**
        ```
        For the Finnish Happiness Factor Finder project (described in the main project `README.md`), we plan a [describe your architecture, e.g., 'web application with a backend for data processing and a frontend for displaying charts, using {mention your preferred language/framework if you have one, otherwise leave open}'].
        1. Is this MVP feasible in 2 hours?
        2. Suggest key libraries/modules for data handling, analysis, and visualization that would integrate well with our chosen (or a suitable) technology stack?
        3. Outline the main functional modules or components we'd need to create.
        ```

### 2.3. Define Architecture & Tech Stack
Based on the brainstorming, your team should decide on:
* The high-level architecture.
* The primary programming language(s) and key frameworks/libraries.
Documenting these choices is the next step.

### 2.4. Create Project Specification Documentation
Clear specifications are vital for guiding both your team and Copilot. These documents should be created collaboratively and iteratively.

**Workflow for Creating Specification Documents:**
It's recommended to create these specification files (`ARCHITECTURE.md`, `BACKLOG.md`, `PROJECT_SPEC.md`) individually.
1.  Discuss the content for each section/file as a team.
2.  Use Copilot Chat, particularly with **Copilot Edits** (e.g., using `#file` or `#selection` in Copilot Chat to target specific files/parts of files), to help draft, update, and refine each document.
3.  Manually create the `docs/specifications/` folder and the empty markdown files first. This makes it easier for Copilot Edits to target them.

**Key Specification Files:**

* **1. Architecture Diagram (`docs/specifications/ARCHITECTURE.md`):**
    * **Purpose:** Visually represent your chosen application architecture.
    * **Content:** Use text-based diagramming tools like Mermaid JS, PlantUML, or even a clear textual outline of components and their interactions.
    * **Example Prompt (Copilot Chat with Edits for `ARCHITECTURE.md`):**
        ```
        #file docs/specifications/ARCHITECTURE.md
        Based on our decision to build a [e.g., 'CLI application that ingests CSVs and API data, processes it, and saves chart images'], help me draft a Mermaid JS sequence diagram or component diagram illustrating the main components (e.g., data ingestion, analysis engine, visualization generator) and data flow.
        ```

* **2. Feature Backlog (`docs/specifications/BACKLOG.md`):**
    * **Purpose:** List the features required for the MVP, broken down into manageable tasks.
    * **Content:** A list of features/user stories. Prioritize for the MVP.
    * **Example Prompt (Copilot Chat with Edits for `BACKLOG.md`):**
        ```
        #file docs/specifications/BACKLOG.md
        Based on the Finnish Happiness Factor Finder MVP requirements, help me create a feature backlog. Key MVP tasks include:
        - Load WHR2024.csv data.
        - Load EdibleFoods-1961-2011.csv data.
        - Implement fetching for 'Education by Gender, Age, and Field' from StatFin PxWeb API.
        - Perform correlation: 'Ladder score' vs. 'Logged GDP per capita'.
        - Visualize this correlation and save as an image.
        Break these down into clear backlog items.
        ```

* **3. Main Project Specification (`docs/specifications/PROJECT_SPEC.md`):**
    * **Purpose:** A central document summarizing key decisions and linking to other detailed specifications.
    * **Location:** `docs/specifications/PROJECT_SPEC.md`
    * **Content Outline:**
        * Project Goal (briefly, from the main `README.md`)
        * Reference to Architecture Diagram: "See `docs/specifications/ARCHITECTURE.md`"
        * Reference to Feature Backlog: "See `docs/specifications/BACKLOG.md`"
        * Chosen Technology Stack (specific languages, libraries, frameworks)
        * Key Modules/Components & Their Primary Responsibilities (high-level textual description)
    * **Example Prompt (Copilot Chat with Edits for `PROJECT_SPEC.md`, after drafting ARCHITECTURE and BACKLOG):**
        ```
        #file docs/specifications/PROJECT_SPEC.md
        Help me create the main project specification.
        It should include:
        - Project Goal (summary for Finnish Happiness Factor Finder).
        - A reference to `docs/specifications/ARCHITECTURE.md` for the architecture diagram.
        - A reference to `docs/specifications/BACKLOG.md` for the feature backlog.
        - Our chosen Technology Stack: [e.g., Python, Pandas, Matplotlib, Requests].
        - A brief outline of Key Modules/Components: [e.g., Data Ingestion, Data Analysis, Visualization].
        ```

---

## 3. Phase 2: Setup for Copilot-Driven Implementation (Approx. 15 minutes)

With a plan in place, configure your environment to maximize Copilot's effectiveness.

### 3.1. Version Control with Git
Initialize Git and commit frequently: `git init`, `git add .`, `git commit -m "Initial planning and specification documents created"`. Regular commits are your safety net.

### 3.2. Global Copilot Instructions (`.github/copilot-instructions.md`)
This file provides project-wide, persistent context to Copilot in VS Code, guiding its behavior across all interactions.
* **Location:** `.github/copilot-instructions.md`
* **Example Content:**
    ```markdown
    ## Project: Finnish Happiness Factor Finder

    **Overall Goal:** Build an application to analyze and visualize data to understand factors contributing to Finland's happiness.
    **Core Requirements Document:** Refer to the main project description `README.md`.
    **MVP Technical Specification:** Detailed in `docs/specifications/PROJECT_SPEC.md`.

    **Key Data Context (for quick reference by inline chat/edit modes):**
    * **`data/WHR2024.csv`**: Contains World Happiness Report 2024 data.
        * **Key Columns:** `Country name`, `Year`, `Ladder score` (main happiness indicator), `Logged GDP per capita`, `Social support`, `Healthy life expectancy`, `Freedom to make life choices`, `Generosity`, `Perceptions of corruption`.
        * **Focus:** This is the primary source for happiness scores and their main correlates.
    * **`data/EdibleFoods-1961-2011.csv`**: Contains FAOSTAT food supply data.
        * **Timeframe:** 1961-2011.
        * **Key Columns:** `Area` (country, e.g., 'Finland'), `Item` (specific food product), `Element` (e.g., `Food supply quantity (kg/capita/yr)`, `Food supply (kcal/capita/day)`), `Year`, `Value`.
        * **Focus:** Use to explore potential links between national food supply patterns and happiness over time. Note the data ends in 2011.
    * **Statistics Finland (PxWeb API):** When asked to implement fetching from this source, refer to specific Python examples in `README.md` or `docs/tasks/` for chosen indicators like education data. This data is typically more granular and specific to Finland.

    ## Role: AI Pair Programmer

    You are assisting developers in a 2-hour workshop to build an MVP (Minimum Viable Product) based *only* on the provided project documents and explicit instructions.

    ## General Instructions for All Interactions:

    1.  **Scope Adherence:** Implement *only* features or code explicitly requested in the current prompt OR detailed in referenced specification documents (`README.md`, `docs/specifications/PROJECT_SPEC.md`, or specific task files in `docs/tasks/`). Do NOT add extra features or deviate without instruction.
    2.  **Clarify Ambiguity:** If a request is unclear, or if you believe a significantly better MVP-aligned alternative exists, briefly state your reasoning and ask for confirmation before proceeding.
    3.  **Clarity & Simplicity First:** Generate code that is readable, well-commented (for complex logic), and suitable for a timed workshop. Avoid overly complex or obscure solutions.
    4.  **Documentation is Truth:** Prioritize instructions and specifications from `README.md` and files in the `docs/` directory.
    5.  **Tech Stack Adherence:** The team's chosen technology stack is defined in `docs/specifications/PROJECT_SPEC.md`. Adhere to these choices.
    6.  **Basic Error Handling:** Include simple `try-except` blocks for operations like file I/O or API calls, printing informative error messages.
    7.  **Data File Paths:** Assume pre-downloaded data files are located in a `data/` directory relative to the project root (e.g., `data/WHR2024.csv`).
    8.  **PxWeb API Implementation:** When implementing PxWeb API calls, base the implementation *strictly* on the examples provided in the project documentation for the specific dataset requested. Do not attempt to build generic PxWeb clients unless specified.
    ```

### 3.3. Guiding Documents for Copilot Agent Mode & Complex Tasks

For effective use of Copilot Agent mode or for guiding complex implementations in Chat, you'll use two types of documents:

1.  **A Generic Agent Workflow (`docs/instructions/agent_workflow.md`):**
    This file defines the *standard operational procedure* for Copilot Agent when it's asked to implement any task. You'll create this once. It tells Copilot *how* to approach its work generally.

2.  **Specific Task Documents (e.g., `docs/tasks/TASK_NAME.md`):**
    For each significant feature from your `BACKLOG.md`, create a small markdown file. This file details the *specific requirements* for that task (what to build, which modules, specific functions, etc.) and will instruct Copilot to follow the generic workflow. The "Assigned Role" in the example below is illustrative and should be adapted per task.

**Example 1: Generic Agent Workflow File**
* **Location:** `docs/instructions/agent_workflow.md`
* **Content:**
    ```markdown
    ## Agent Mode - General Implementation Workflow

    This document outlines the standard operational procedure for GitHub Copilot Agent when tasked with implementing features or modules for this project.

    1.  **Understand Task & Context:**
        * Review the specific task requirements provided in the prompt or referenced task document (e.g., from `docs/tasks/`).
        * Refer to `docs/specifications/PROJECT_SPEC.md` for overall project architecture, technology stack, and MVP goals.
        * Refer to `.github/copilot-instructions.md` for global project conventions.
    2.  **Assessment & Planning:**
        * Before writing new code, briefly assess if any existing code in the target module(s) can be reused, needs refactoring to accommodate the new task, or might conflict.
        * Note any dependencies on other modules or unfulfilled prerequisites for the current task.
    3.  **Adherence to Specifications:**
        * Implement *only* the features, functions, and logic described in the specific task document and `docs/specifications/PROJECT_SPEC.md`.
    4.  **Deviation Protocol:**
        * If you believe a deviation from the specified requirements, outlined steps, or chosen technologies (as per `PROJECT_SPEC.md`) is strongly necessary or highly beneficial for achieving the task's goal:
            * Clearly state your proposed deviation.
            * Provide a concise justification (e.g., improves performance, simplifies code significantly, necessary for compatibility).
            * **Explicitly ask for permission/confirmation before implementing the deviation.** Await a "Proceed with deviation" or similar response. If no permission is given, adhere to the original specification.
    5.  **Code Implementation:**
        * Write clear, concise, and well-commented code (especially for non-obvious logic) according to the specific task requirements.
        * Follow language-specific best practices and any style guides mentioned in `PROJECT_SPEC.md` or `.github/copilot-instructions.md`.
    6.  **Post-Implementation Quality Checks (Simulated for Workshop):**
        * **(Linting):** Assume generated code is checked with a standard linter/formatter for the language. Aim to produce code that would pass.
        * **(Testing):** Assume relevant unit tests (if pre-defined or generated as part of the task) are executed. Aim to produce code that would pass these tests.
        * **(Fixes):** If (simulated) linting errors or test failures are implied or identified, attempt to fix the generated code.
    7.  **Output:**
        * Provide the complete code for the specified module(s) or the functions/classes implemented as per the task.
        * If changes were made to existing files (beyond adding new code), clearly indicate these changes.
    8.  **Git Commit (Simulated for Workshop):**
        * After successful implementation and (simulated) checks, a Git commit would typically be made.
        * The commit message should be concise, imperative, and accurately describe the change (e.g., "feat: [description of feature]"). Maximum 160 characters. Indicate this simulated commit message in your response.
    ```

**Example 2: Specific Task Document**
* **Location (example):** `docs/tasks/IMPLEMENT_DATA_LOADERS.md`
* **Content:**
    ```markdown
    ## Task: Implement Core Data Loaders

    **Workflow Reference:** When implementing this task, adhere to the general procedure outlined in `docs/instructions/agent_workflow.md`.

    **Project Specification Reference:** `docs/specifications/PROJECT_SPEC.md`
    **Target Module(s):** `src/data_loader.py` (create if absent)
    **Assigned Role:** Python data engineering specialist.
    **Goal:** Create functions to load pre-downloaded CSV datasets (`data/WHR2024.csv`, `data/EdibleFoods-1961-2011.csv`) and a function to fetch specified StatFin education data via PxWeb API, saving it locally.

    ---
    **Specific Requirements & Acceptance Criteria for this Task:**

    1.  Ensure the module `src/data_loader.py` is created if it doesn't exist.
    2.  Import necessary libraries: `pandas`, `requests`, `json`, `os`.
    3.  **Function `load_whr_data(filepath='data/WHR2024.csv')`:**
        * **Action:** Reads the CSV file specified by `filepath` into a Pandas DataFrame.
        * **Error Handling:** Implements a `try-except FileNotFoundError` block. If the file is not found, it should print an informative error message to the console and return `None`.
        * **Return:** The Pandas DataFrame if successful, `None` otherwise.
    4.  **Function `load_food_data(filepath='data/EdibleFoods-1961-2011.csv')`:**
        * **Action:** Reads the CSV file specified by `filepath` into a Pandas DataFrame.
        * **Error Handling:** Implements a `try-except FileNotFoundError` block. If the file is not found, it should print an informative error message to the console and return `None`.
        * **Return:** The Pandas DataFrame if successful, `None` otherwise.
    5.  **Function `Workspace_statfin_education_data()`:**
        * **Action:** Implements Python code (based on the PxWeb API example for "Statistics Finland: Education by Gender, Age, and Field" detailed in the main project `README.md` or `PROJECT_SPEC.md`) to fetch the specified education dataset.
        * Ensures the `data` directory exists using `os.makedirs('data', exist_ok=True)` before saving.
        * Saves the fetched JSON data to `data/statfin_vkour_pxt_12br.json`.
        * **Error Handling:** Implements a `try-except requests.exceptions.RequestException` block for the API call. If an error occurs, it should print an informative error message to the console and return `None`.
        * **Return:** The fetched JSON data (from `response.json()`) if successful, `None` otherwise.
    6.  **Scope:** This module must *only* contain data loading and fetching logic. No data cleaning, transformation (beyond what the API provides), or analysis should be performed within these functions.
    ```

## 4. Phase 3: Iterative Implementation with Copilot (Approx. 45-55 minutes)

Now, translate your plans and specifications into code with Copilot's assistance.

### 4.1. Implement Bare Bones
Use Copilot Chat to kick off implementation, referencing your documentation. For more automated execution, especially if using Copilot Agent mode (e.g., commands like `/new` in Copilot Chat if they invoke agent-like behaviors, or other dedicated Agent features), clearly separating the task specification from the general workflow is key.

Your prompt should clearly state which document contains the *task details* and which contains the *general implementation process*.

* **Example Prompt (Copilot Chat, guiding Copilot Agent mode or a comprehensive chat interaction):**
    ```
    @workspace
    I need you to implement the data loading functionality for our project.

    **Task Specification:** The detailed requirements for what to build (modules, functions, specific logic) are located in:
    `docs/tasks/IMPLEMENT_DATA_LOADERS.md`

    **Implementation Workflow:** The general instructions on how you should approach the implementation (assessment, deviation protocol, quality checks, commit simulation, etc.) are defined in:
    `docs/instructions/agent_workflow.md`

    Please proceed with implementing the full task as described in `docs/tasks/IMPLEMENT_DATA_LOADERS.md`, ensuring you strictly follow the general workflow outlined in `docs/instructions/agent_workflow.md`.
    Start by ensuring the `src/data_loader.py` file exists or is created, then implement the functions one by one as specified.
    ```
   **Note for step-by-step in Chat:** If you prefer a more conversational, step-by-step approach within Copilot Chat (rather than asking for the whole task at once), you can still refer to both documents. For example:
    ```
    @workspace
    Let's start implementing the `load_whr_data()` function from `docs/tasks/IMPLEMENT_DATA_LOADERS.md`. Remember to follow the general process defined in `docs/instructions/agent_workflow.md`.
    ```

### 4.2. Work Through Backlog
Address items from your `docs/specifications/BACKLOG.md`. For each significant item:
1.  Create a new specific task document in `docs/tasks/` (e.g., `IMPLEMENT_CORRELATION_ANALYSIS.md`).
2.  In this task document, reference the `docs/instructions/agent_workflow.md`.
3.  Detail the specific requirements, inputs, outputs, and acceptance criteria for that task.
4.  Use Copilot Chat (with `@workspace` and by referencing your task document) or Copilot Agent mode to implement the task.

### 4.3. Code Testing
Verify Copilot's output and your own code.
* **TDD (Test-Driven Development) Approach:** Consider writing a basic test outline *before* asking Copilot to generate the function code.
* **Tests After Implementation:** At minimum, write tests after code generation to confirm functionality.
* **Example Prompt (Copilot Chat for writing tests):**
    ```
    @workspace
    For the function `load_whr_data()` in `src/data_loader.py` (which you helped implement), help me write `pytest` unit tests in a new file `tests/test_data_loader.py`. The tests should check for:
    1. Correct loading of `data/WHR2024.csv` into a non-empty Pandas DataFrame.
    2. Proper handling of `FileNotFoundError` if the CSV is missing.
    ```

### 4.4. Review, Refactor, Commit Loop
* **Review:** Always critically review code generated by Copilot. Does it meet requirements? Is it efficient? Is it secure?
* **Refactor:** Don't hesitate to refactor the code for clarity, performance, or better organization. You can ask Copilot for refactoring suggestions.
* **Commit:** Commit working changes to Git frequently with clear messages.

## 5. Phase 4: Wrap-up & Presentation Prep (Approx. 15 minutes)

* Finalize the MVP features as per your `BACKLOG.md`.
* Ensure the application runs.
* Prepare a brief demonstration of your application and your development process with Copilot.

## 6. Key Takeaways: AI Collaboration Workflow (Approx. 5 minutes)

* **Clarity is King:** Effective AI collaboration relies on clear, unambiguous, and well-structured documented specifications and workflows.
* **Documentation as a Tool:** Use documents like `PROJECT_SPEC.md`, `agent_workflow.md`, and specific task files not just for human understanding, but as direct input and guidance for AI.
* **Iterative Refinement:** Your first prompt or Copilot's first output might not be perfect. Iterate on your instructions and the code.
* **Developer in Control:** You are the lead developer. Review, understand, test, and own all code, whether written by you or with AI assistance.
* **Strategic Prompting:** Global instructions (`.github/copilot-instructions.md`) and well-crafted task-specific prompts significantly improve Copilot's output quality and relevance.