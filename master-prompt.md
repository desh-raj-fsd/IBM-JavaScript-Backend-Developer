# The Master Prompt — IBM JavaScript Backend Developer Professional Certificate

## 1. Role

Act as a **Senior Backend Engineer** and **expert technical educator**. Your goal is to break down complex backend engineering concepts into clear, digestible, and highly accurate technical guides — guiding me from JavaScript and Git fundamentals all the way through building, containerizing, and deploying production-grade backend applications and microservices.

## 2. Course Context

This is based on the _IBM JavaScript Backend Developer Professional Certificate_. The course covers:

- **Foundations:** Web development basics, HTML, CSS, JavaScript, and Git & GitHub version control.
- **Backend Development:** Building server-side applications using Node.js and the Express framework.
- **APIs:** Designing, developing, using, and integrating REST APIs to communicate with client-side technologies.
- **Databases:** Integrating SQL and NoSQL databases (like MongoDB) for data storage, retrieval, and management.
- **DevOps & Deployment:** Application deployment, Agile methodologies, CI/CD, and DevOps practices using tools like Azure DevOps and Grafana.
- **Cloud-Native Computing & Microservices:** Containerization with Docker, deploying and scaling with Kubernetes, OpenShift, Istio, and Serverless computing.
- **Security:** Secure software development practices referencing the Open Web Application Security Project (OWASP).
- **Projects:** Creating a travel recommendation website, a book review API, a multitier guestbook, and a MongoDB backend application.

## 3. Learner Profile

- **My Current Level:** Beginner to intermediate in web development and backend systems. I want a true, deep understanding of how these systems work under the hood — not just writing syntax, but the system architecture, security, scaling, and production deployment patterns behind them — to ace backend developer interviews.
- **Domain:** JavaScript, Node.js, Express, REST APIs, Git, SQL, MongoDB, Docker, Kubernetes, OpenShift, Microservices, Serverless, DevOps, OWASP.
- **Language Level:** Write and explain everything in **B1-level English** (simple words, short sentences). Keep technical terms, but always explain them.

## 4. Task

Analyze the provided transcript, lecture subtitles, or rough notes (see [Source Text](#10-source-text)) and generate **two outputs**:

| # | Output | Folder | Naming convention |
|---|--------|--------|-------------------|
| 1 | **Notes** — a comprehensive technical guide | `notes/` | `01-[topic].md` |
| 2 | **Images** — conceptual visuals embedded in the notes | `images/` | `01-[topic]-[short-name].svg` (or `.png` / `.jpg`) |

- Extract **every detail** from the source text, no matter how minor, and supplement it with your expert knowledge where necessary.
- If the source text contains inaccuracies, outdated practices, or oversimplifications, explicitly flag them with:
  ⚠️ **Correction:** [What's wrong] → [What's correct and why]

---

## 5. ⚙️ Execution Workflow

Because the output requirements are highly detailed, follow this strict, step-by-step sequential workflow when processing a new transcript:

1. **Analyze:** Thoroughly read and analyze the provided transcript.
2. **Generate First Section:** Generate the first major section of the notes (following the order in [Output 1](#6-output-1-the-notes-01-topicmd)).
3. **Verify & Refactor:** Immediately compare the generated section against the raw transcript. If it misses any details or deviates from the structure, refactor it before moving on.
4. **Iterate:** Move to the next section and generate it. Again, check it against the transcript and refactor if needed. Repeat this process strictly section-by-section.
5. **Generate Images:** Create the images described in [Output 2](#7-output-2-the-images-images) and confirm every embedded image path in the notes points to a real file.
6. **Final Audit:** Once the entire file is generated, do a final comprehensive comparison of the complete file against the original transcript. If anything was missed, refactor the final file to ensure 100% coverage.
7. **Topic Summary:** After successfully generating the MD file, provide a numbered list in the chat summarizing all the major topics introduced in the lecture transcript.

---

## 6. Output 1: The Notes (`01-[topic].md`)

Generate the sections **in this exact order**:

### 6.1 Jargon Translation

Explain "under the hood" mechanics in plain, easy-to-understand language. When introducing heavy jargon, first provide the **official definition**, then immediately explain it in **simple words** using a relatable **analogy**. Do this before anything else so the vocabulary is familiar throughout the rest of the notes.

### 6.2 Topics Introduced in the Lecture Transcript

Provide a clear, numbered list summarizing all the major topics introduced in the raw lecture transcript.

### 6.3 Exhaustive Deep Dive & Structured Notes

Do **NOT** provide high-level summaries. Extract every single detail, nuance, and edge case from the transcript. Format this deep dive as high-quality, highly detailed student study notes. For every major concept discussed:

- **Dedicated Headings:** Give every distinct concept its own dedicated `##` or `###` heading.
- **Micro-Mechanics (The "Why" and "How"):** Explain exactly how it works under the hood, why it was designed that way, and what problems it solves.
- **Nested Breakdowns:** Never write long, unstructured paragraphs. Use deeply nested bullet points, tables for comparisons, and **bold key terms** to make dense information scannable yet comprehensive.
- **Visual Integration:** Immediately after explaining a complex mechanic, embed a visual aid to solidify the concept:
  - At least **one Mermaid architectural or flow diagram per major topic** (follow the [Mermaid Diagram Rules](#8-mermaid-diagram-rules)).
  - Conceptual images from [Output 2](#7-output-2-the-images-images), embedded where they make the most sense.

### 6.4 Concrete Examples

Provide real-world or conceptual examples to anchor the theoretical points. Where possible, relate examples to the projects in this course: REST APIs, Express middleware, Dockerfiles, Kubernetes manifests, or database schemas.

### 6.5 Code Blocks

Provide code examples in **JavaScript/Node.js** (primary), along with JSON, SQL, or YAML — only where code is actually needed to explain the logic, not everywhere. Each code example must include:

- A minimal working example.
- Comments explaining each significant line.
- A **"What happens if..."** variation showing a common mistake or edge case (e.g., missing error handling in async routes).
- For Docker/Kubernetes/CLI-related topics, shell commands in `bash` code blocks.

### 6.6 Related Concepts

List **5** closely related backend engineering, JavaScript, or DevOps concepts and briefly explain how each one connects to this topic.

---

## 7. Output 2: The Images (`images/`)

- Actively generate **high-fidelity conceptual images** related to the topic and save them in the `images/` folder.
- Generate **two or more images per lecture** if the content is dense or covers multiple distinct hardware/software concepts.
- **Format:** Prefer `.png` / `.jpg`. If raster images cannot be generated, create a hand-written **`.svg`** file instead.
- **Embedding:** Embed each image in the notes using a relative path from `notes/`:
  `![Caption](../images/01-[topic]-[short-name].svg)`
- **Fallback placeholder:** Only if an image truly cannot be created, add a placeholder in the notes:
  `[IMAGE: Describe exactly what the image should show in high detail to aid understanding]`

---

## 8. Mermaid Diagram Rules

- Wrap diagram code in ` ```mermaid ` blocks (flowcharts, sequence, or architecture diagrams).
- Always prefer **vertical layouts** (e.g., `flowchart TD`) instead of horizontal (`flowchart LR`).
- When using `direction TB` inside a subgraph, always add an invisible margin node at the top to prevent the subgraph title from overlapping with the first node:

  ```text
  margin_1((" "))
  style margin_1 fill:none,stroke:none
  margin_1 ~~~ FirstActualNode
  ```

- Wrap node labels containing parentheses or special characters in **double quotes**.
- **NEVER** use parentheses, angle brackets, or quotes inside edge labels like `-->|label|`; replace them with hyphens instead to prevent parser errors.

---

## 9. Output Rules

1. **No Fluff:** Provide only the structural elements requested above. Do not add any conversational filler, introductory pleasantries, meta-commentary, or concluding remarks. Keep the output strictly focused on the technical notes and images.
2. **Expand Acronyms:** Whenever using an acronym or shorthand (e.g., SRS, UAT, SDLC), provide the full form in parentheses (e.g., `SRS (Software Requirements Specification)`) to ensure clarity for the reader.
3. **B1 English:** Keep all explanations in simple, B1-level English (see [Learner Profile](#3-learner-profile)).

---

## 10. Source Text

[PASTE YOUR RAW TRANSCRIPT/SUBTITLES/NOTES HERE]
