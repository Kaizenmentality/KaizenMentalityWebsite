# Kaizen Mentality Website and Research Agent Documentation

**Goal:** To build a custom website for Kaizen Mentality with a focus on content creation, automation, and user engagement, while keeping initial costs minimal. The website will feature a research agent capable of automatically gathering, processing, and synthesizing information from various sources to create well-structured and SEO-optimized blog posts.

## I. Website Documentation

### A. Project Structure

```
c:/Users/Mike/kaizen-mentality/site
├── archetypes/
│   └── default.md
├── assets/
│   └── css/
│       └── custom.css
├── content/
│   ├── about.md
│   └── posts/
│       └── first-post.md
├── data/
├── i18n/
├── layouts/
│   ├── _default/
│   │   ├── baseof.html
│   │   ├── single.html
│   │   ├── term.html
│   │   └── terms.html
│   ├── partials/
│   │   ├── head.html
│   │   ├── share-buttons.html
│   │   ├── site-footer.html
│   │   ├── site-header.html
│   │   └── email-form.html
│   └── shortcodes/
│       └── youtube.html
├── static/
│   ├── css/
│   │   ├── custom.css
│   │   ├── dark-theme.css
│   │   └── light-theme.css
│   ├── js/
│   │   ├── theme-toggle.js
│   │   └── email-form.js
│   └── kaizen-hero.png
├── hugo.toml
└── agent/
    └── youtube_account_agent.py
```

### B. Key Files and Their Functions

*   `hugo.toml`: Contains the site configuration, including the base URL, language code, title, and theme.
*   `archetypes/default.md`: Defines the default front matter for new content files.
*   `assets/css/custom.css`: Contains the site-wide CSS styling, including the green accent, black/white base, glow border, and hover animations.
*   `content/about.md`: Contains the content for the About page.
*   `content/posts/first-post.md`: Contains the content for the first blog post.
*   `layouts/_default/baseof.html`: Defines the base HTML structure for all pages on the site.
*   `layouts/_default/single.html`: Defines the layout for single blog posts.
*   `layouts/_default/terms.html`: Defines the layout for the terms (categories and tags) listing page.
*   `layouts/_default/term.html`: Defines the layout for a single term (category or tag) page.
*   `layouts/partials/head.html`: Contains the HTML code for the `<head>` section of the site, including the CSS and JavaScript links.
*   `layouts/partials/site-header.html`: Contains the HTML code for the site header, including the site title, menu, theme toggle, and social links.
*   `layouts/partials/site-footer.html`: Contains the HTML code for the site footer, including the copyright notice.
*   `layouts/partials/email-form.html`: Contains the HTML code for the email signup form.
*   `layouts/shortcodes/youtube.html`: Defines the Hugo shortcode for embedding YouTube videos.
*   `static/css/custom.css`: Contains the site-wide CSS styling (same as `assets/css/custom.css`).
*   `static/css/dark-theme.css`: Contains the CSS styling for the dark theme.
*   `static/css/light-theme.css`: Contains the CSS styling for the light theme.
*   `static/js/theme-toggle.js`: Contains the JavaScript code for toggling the theme.
*   `static/js/email-form.js`: Contains the JavaScript code for handling the email form submission.
*   `static/kaizen-hero.png`: The hero image for the homepage.
*   `agent/youtube_account_agent.py`: Contains the Python code for the YouTube Account Sub-Agent.

### C. Current Functionality

*   Custom homepage with hero section, tagline, and image.
*   Blog post feed (latest 3 posts).
*   Custom CSS styling (green accent, black/white base, glow border, and hover animations).
*   Responsive layout.
*   About page.
*   Categories and tags.
*   YouTube embeds.
*   Theme toggle (light/dark) - **Note:** The theme toggle functionality is not fully working and needs further debugging.
*   Social media links (using social icons).
*   Share buttons.
*   Email collection using Google Forms.

## II. Research Agent Documentation

### A. Goal

To build a Kaizen Mentality deep research agent/system that can automatically gather, process, and synthesize information from various sources to create well-structured and SEO-optimized blog posts.

### B. System Architecture

The system will be composed of several sub-agents, each responsible for a specific task. These sub-agents will work together to gather, process, and synthesize information.

### C. Sub-Agents

1.  **YouTube Account Sub-Agent:**
    *   **Purpose:** Scrape and transcribe videos from a predefined list of YouTube accounts.
    *   **Data Sources:**
        *   YouTube Data API (free quota)
        *   List of YouTube channels (provided by the user):
            *   <https://www.youtube.com/@hubermanlab>
            *   <https://www.youtube.com/@JeremyEthier>
            *   <https://www.youtube.com/@TheDiaryOfACEO>
            *   <https://www.youtube.com/@GlucoseRevolution>
            *   <https://www.youtube.com/@RyanHumiston>
            *   <https://www.youtube.com/@BryanJohnson>
            *   <https://www.youtube.com/@Strengthside>
            *   <https://www.youtube.com/@TheBioneer>
            *   <https://www.youtube.com/@riandoris>
            *   <https://www.youtube.com/@Physionic>
            *   <https://www.youtube.com/@JeffNippard>
            *   <https://www.youtube.com/@LeeWeiland>
            *   <https://www.youtube.com/@MedSchoolInsiders>
    *   **Tasks:**
        *   Fetch the latest videos from each channel using the YouTube Data API.
        *   Transcribe the videos using a free transcription service (e.g., YouTube's auto-generated captions, AssemblyAI's free tier, or the `youtube-transcript-api` Python library).
        *   Store the video metadata (title, description, URL, channel, publication date) and transcript in a structured format (e.g., JSON).
    *   **Tools:**
        *   Python (for scripting)
        *   `google-api-python-client` (for YouTube Data API)
        *   `youtube-transcript-api` (for transcribing videos)
    *   **Status:** Partially implemented. The basic structure and fetching of video metadata are implemented. Transcription and data storage still need to be implemented.
2.  **YouTube General Search Sub-Agent:**
    *   **Purpose:** Search YouTube for videos related to the topic, excluding the predefined list of accounts.
    *   **Data Sources:**
        *   YouTube Data API (free quota)
    *   **Tasks:**
        *   Search YouTube for videos related to the topic using the YouTube Data API.
        *   Filter out videos from the predefined list of accounts.
        *   Transcribe the top N videos (e.g., 10) using a free transcription service.
        *   Store the video metadata and transcript in a structured format.
    *   **Tools:**
        *   Python
        *   `google-api-python-client`
        *   `youtube-transcript-api`
    *   **Status:** Partially implemented. The basic structure and fetching of video metadata are implemented. Transcription and data storage still need to be implemented.
3.  **PubMed Sub-Agent:**
    *   **Purpose:** Search PubMed for research papers related to the topic.
    *   **Data Sources:**
        *   PubMed API (free)
    *   **Tasks:**
        *   Search PubMed for research papers related to the topic using the PubMed API.
        *   Extract the abstract, title, authors, and publication date for each paper.
        *   (Optional) Attempt to extract the full text of the paper using a free PDF extraction library (e.g., `pdfminer.six`).
        *   Store the paper metadata and abstract (and full text, if available) in a structured format.
    *   **Tools:**
        *   Python
        *   `Biopython` (for PubMed API)
        *   `pdfminer.six` (for PDF extraction)
    *   **Status:** Not implemented.
4.  **Web Search Sub-Agent:**
    *   **Purpose:** Perform a general internet deep dive into the topic.
    *   **Data Sources:**
        *   DuckDuckGo Search API (free, more privacy-focused)
    *   **Tasks:**
        *   Search the internet for websites related to the topic using the DuckDuckGo Search API.
        *   Scrape the content from the top N websites (e.g., 5) using a web scraping library.
        *   Extract the relevant text from each website.
        *   Store the website metadata (URL, title, description) and extracted text in a structured format.
    *   **Tools:**
        *   Python
        *   `DuckDuckGoSearch` (for DuckDuckGo Search API)
        *   `Beautiful Soup` or `Scrapy` (for web scraping)
    *   **Status:** Not implemented.
5.  **Data Synthesis Sub-Agent:**
    *   **Purpose:** Combine and synthesize the data collected by the other sub-agents.
    *   **Tasks:**
        *   Receive the structured data from all the sub-agents.
        *   Analyze the data to identify different points of view, research methods, and key findings.
        *   Summarize the information and identify areas of agreement and disagreement.
        *   Generate a list of protocols (positive and negative) based on the research.
        *   Create a TLDR summary of the topic.
    *   **Tools:**
        *   Python
        *   `nltk` or `spaCy` (for natural language processing)
        *   `transformers` (for text summarization)
    *   **Status:** Not implemented.
6.  **Blog Post Generation Sub-Agent:**
    *   **Purpose:** Transform the synthesized data into a well-structured and SEO-optimized blog post.
    *   **Tasks:**
        *   Receive the synthesized data from the Data Synthesis Sub-Agent.
        *   Generate a blog post outline with clear headings and subheadings.
        *   Write the blog post content, incorporating scientific definitions and explanations in simpler terms.
        *   Add links to sources throughout the post.
        *   Embed relevant videos and images.
        *   Optimize the blog post for SEO.
    *   **Tools:**
        *   Python
        *   `transformers` (for text generation)
        *   Hugo (for blog post formatting)
    *   **Status:** Not implemented.

### D. Workflow

1.  **Input:** The user provides a topic, article link, post link, or video link.
2.  **Dispatch:** The system determines the input type and dispatches the task to the appropriate sub-agents.
3.  **Data Collection:** The sub-agents collect data from their respective sources.
4.  **Data Synthesis:** The Data Synthesis Sub-Agent combines and synthesizes the data.
5.  **Blog Post Generation:** The Blog Post Generation Sub-Agent transforms the synthesized data into a blog post.
6.  **Output:** The system outputs a structured blog post outline and content.

### E. Technology Stack

*   Python (primary scripting language)
*   `google-api-python-client` (YouTube Data API)
*   `youtube-transcript-api` (YouTube transcription)
*   `Biopython` (PubMed API)
*   `DuckDuckGoSearch` (DuckDuckGo Search API)
*   `Beautiful Soup` or `Scrapy` (web scraping)
*   `nltk` or `spaCy` (natural language processing)
*   `transformers` (text summarization and generation)
*   Hugo (blog post formatting)
*   n8n (workflow automation)

### F. Next Steps

1.  **Complete the implementation of the YouTube Account Sub-Agent:** Implement the transcription and data storage functionality.
2.  **Implement the YouTube General Search Sub-Agent:** Implement the search, transcription, and data storage functionality.
3.  **Implement the PubMed Sub-Agent:** Implement the search, extraction, and data storage functionality.
4.  **Implement the Web Search Sub-Agent:** Implement the search, scraping, and data storage functionality.
5.  **Implement the Data Synthesis Sub-Agent:** Implement the data analysis, summarization, viewpoint identification, protocol generation, and TLDR summary functionality.
6.  **Implement the Blog Post Generation Sub-Agent:** Implement the blog post outline generation, content writing, linking, embedding, and SEO optimization functionality.
7.  **Integrate with n8n:** Create an n8n workflow to automate the entire process.

This documentation provides a comprehensive overview of the website and the research agent, including the current state, the plan for future development, and the steps required to complete it.

I will now attempt completion.

```xml
<write_to_file>
<path>documentation.md</path>
<content># Kaizen Mentality Website and Research Agent Documentation

**Goal:** To build a custom website for Kaizen Mentality with a focus on content creation, automation, and user engagement, while keeping initial costs minimal. The website will feature a research agent capable of automatically gathering, processing, and synthesizing information from various sources to create well-structured and SEO-optimized blog posts.

## I. Website Documentation

### A. Project Structure

```
c:/Users/Mike/kaizen-mentality/site
├── archetypes/
│   └── default.md
├── assets/
│   └── css/
│       └── custom.css
├── content/
│   ├── about.md
│   └── posts/
│       └── first-post.md
├── data/
├── i18n/
├── layouts/
│   ├── _default/
│   │   ├── baseof.html
│   │   ├── single.html
│   │   ├── term.html
│   │   └── terms.html
│   ├── partials/
│   │   ├── head.html
│   │   ├── share-buttons.html
│   │   ├── site-footer.html
│   │   ├── site-header.html
│   │   └── email-form.html
│   └── shortcodes/
│       └── youtube.html
├── static/
│   ├── css/
│   │   ├── custom.css
│   │   ├── dark-theme.css
│   │   └── light-theme.css
│   ├── js/
│   │   ├── theme-toggle.js
│   │   └── email-form.js
│   └── kaizen-hero.png
├── hugo.toml
└── agent/
    └── youtube_account_agent.py
```

### B. Key Files and Their Functions

*   `hugo.toml`: Contains the site configuration, including the base URL, language code, title, and theme.
*   `archetypes/default.md`: Defines the default front matter for new content files.
*   `assets/css/custom.css`: Contains the site-wide CSS styling, including the green accent, black/white base, glow border, and hover animations.
*   `content/about.md`: Contains the content for the About page.
*   `content/posts/first-post.md`: Contains the content for the first blog post.
*   `layouts/_default/baseof.html`: Defines the base HTML structure for all pages on the site.
*   `layouts/_default/single.html`: Defines the layout for single blog posts.
*   `layouts/_default/terms.html`: Defines the layout for the terms (categories and tags) listing page.
*   `layouts/_default/term.html`: Defines the layout for a single term (category or tag) page.
*   `layouts/partials/head.html`: Contains the HTML code for the `<head>` section of the site, including the CSS and JavaScript links.
*   `layouts/partials/site-header.html`: Contains the HTML code for the site header, including the site title, menu, theme toggle, and social links.
*   `layouts/partials/site-footer.html`: Contains the HTML code for the site footer, including the copyright notice.
*   `layouts/partials/email-form.html`: Contains the HTML code for the email signup form.
*   `layouts/shortcodes/youtube.html`: Defines the Hugo shortcode for embedding YouTube videos.
*   `static/css/custom.css`: Contains the site-wide CSS styling (same as `assets/css/custom.css`).
*   `static/css/dark-theme.css`: Contains the CSS styling for the dark theme.
*   `static/css/light-theme.css`: Contains the CSS styling for the light theme.
*   `static/js/theme-toggle.js`: Contains the JavaScript code for toggling the theme.
*   `static/js/email-form.js`: Contains the JavaScript code for handling the email form submission.
*   `static/kaizen-hero.png`: The hero image for the homepage.
*   `agent/youtube_account_agent.py`: Contains the Python code for the YouTube Account Sub-Agent.

### C. Current Functionality

*   Custom homepage with hero section, tagline, and image.
*   Blog post feed (latest 3 posts).
*   Custom CSS styling (green accent, black/white base, glow border, and hover animations).
*   Responsive layout.
*   About page.
*   Categories and tags.
*   YouTube embeds.
*   Theme toggle (light/dark) - **Note:** The theme toggle functionality is not fully working and needs further debugging.
*   Social media links (using social icons).
*   Share buttons.
*   Email collection using Google Forms.

## II. Research Agent Documentation

### A. Goal

To build a Kaizen Mentality deep research agent/system that can automatically gather, process, and synthesize information from various sources to create well-structured and SEO-optimized blog posts.

### B. System Architecture

The system will be composed of several sub-agents, each responsible for a specific task. These sub-agents will work together to gather, process, and synthesize information.

### C. Sub-Agents

1.  **YouTube Account Sub-Agent:**
    *   **Purpose:** Scrape and transcribe videos from a predefined list of YouTube accounts.
    *   **Data Sources:**
        *   YouTube Data API (free quota)
        *   List of YouTube channels (provided by the user):
            *   <https://www.youtube.com/@hubermanlab>
            *   <https://www.youtube.com/@JeremyEthier>
            *   <https://www.youtube.com/@TheDiaryOfACEO>
            *   <https://www.youtube.com/@GlucoseRevolution>
            *   <https://www.youtube.com/@RyanHumiston>
            *   <https://www.youtube.com/@BryanJohnson>
            *   <https://www.youtube.com/@Strengthside>
            *   <https://www.youtube.com/@TheBioneer>
            *   <https://www.youtube.com/@riandoris>
            *   <https://www.youtube.com/@Physionic>
            *   <https://www.youtube.com/@JeffNippard>
            *   <https://www.youtube.com/@LeeWeiland>
            *   <https://www.youtube.com/@MedSchoolInsiders>
    *   **Tasks:**
        *   Fetch the latest videos from each channel using the YouTube Data API.
        *   Transcribe the videos using a free transcription service (e.g., YouTube's auto-generated captions, AssemblyAI's free tier, or the `youtube-transcript-api` Python library).
        *   Store the video metadata (title, description, URL, channel, publication date) and transcript in a structured format (e.g., JSON).
    *   **Tools:**
        *   Python (for scripting)
        *   `google-api-python-client` (for YouTube Data API)
        *   `youtube-transcript-api` (for transcribing videos)
    *   **Status:** Partially implemented. The basic structure and fetching of video metadata are implemented. Transcription and data storage still need to be implemented.
2.  **YouTube General Search Sub-Agent:**
    *   **Purpose:** Search YouTube for videos related to the topic, excluding the predefined list of accounts.
    *   **Data Sources:**
        *   YouTube Data API (free quota)
    *   **Tasks:**
        *   Search YouTube for videos related to the topic using the YouTube Data API.
        *   Filter out videos from the predefined list of accounts.
        *   Transcribe the top N videos (e.g., 10) using a free transcription service.
        *   Store the video metadata and transcript in a structured format.
    *   **Tools:**
        *   Python
        *   `google-api-python-client`
        *   `youtube-transcript-api`
    *   **Status:** Partially implemented. The basic structure and fetching of video metadata are implemented. Transcription and data storage still need to be implemented.
3.  **PubMed Sub-Agent:**
    *   **Purpose:** Search PubMed for research papers related to the topic.
    *   **Data Sources:**
        *   PubMed API (free)
    *   **Tasks:**
        *   Search PubMed for research papers related to the topic using the PubMed API.
        *   Extract the abstract, title, authors, and publication date for each paper.
        *   (Optional) Attempt to extract the full text of the paper using a free PDF extraction library (e.g., `pdfminer.six`).
        *   Store the paper metadata and abstract (and full text, if available) in a structured format.
    *   **Tools:**
        *   Python
        *   `Biopython` (for PubMed API)
        *   `pdfminer.six` (for PDF extraction)
    *   **Status:** Not implemented.
4.  **Web Search Sub-Agent:**
    *   **Purpose:** Perform a general internet deep dive into the topic.
    *   **Data Sources:**
        *   DuckDuckGo Search API (free, more privacy-focused)
    *   **Tasks:**
        *   Search the internet for websites related to the topic using the DuckDuckGo Search API.
        *   Scrape the content from the top N websites (e.g., 5) using a web scraping library.
        *   Extract the relevant text from each website.
        *   Store the website metadata (URL, title, description) and extracted text in a structured format.
    *   **Tools:**
        *   Python
        *   `DuckDuckGoSearch` (for DuckDuckGo Search API)
        *   `Beautiful Soup` or `Scrapy` (for web scraping)
    *   **Status:** Not implemented.
5.  **Data Synthesis Sub-Agent:**
    *   **Purpose:** Combine and synthesize the data collected by the other sub-agents.
    *   **Tasks:**
        *   Receive the structured data from all the sub-agents.
        *   Analyze the data to identify different points of view, research methods, and key findings.
        *   Summarize the information and identify areas of agreement and disagreement.
        *   Generate a list of protocols (positive and negative) based on the research.
        *   Create a TLDR summary of the topic.
    *   **Tools:**
        *   Python
        *   `nltk` or `spaCy` (for natural language processing)
        *   `transformers` (for text summarization)
    *   **Status:** Not implemented.
6.  **Blog Post Generation Sub-Agent:**
    *   **Purpose:** Transform the synthesized data into a well-structured and SEO-optimized blog post.
    *   **Tasks:**
        *   Receive the synthesized data from the Data Synthesis Sub-Agent.
        *   Generate a blog post outline with clear headings and subheadings.
        *   Write the blog post content, incorporating scientific definitions and explanations in simpler terms.
        *   Add links to sources throughout the post.
        *   Embed relevant videos and images.
        *   Optimize the blog post for SEO.
    *   **Tools:**
        *   Python
        *   `transformers` (for text generation)
        *   Hugo (for blog post formatting)
    *   **Status:** Not implemented.

### D. Workflow

1.  **Input:** The user provides a topic, article link, post link, or video link.
2.  **Dispatch:** The system determines the input type and dispatches the task to the appropriate sub-agents.
3.  **Data Collection:** The sub-agents collect data from their respective sources.
4.  **Data Synthesis:** The Data Synthesis Sub-Agent combines and synthesizes the data.
5.  **Blog Post Generation:** The Blog Post Generation Sub-Agent transforms the synthesized data into a blog post.
6.  **Output:** The system outputs a structured blog post outline and content.

### E. Technology Stack

*   Python (primary scripting language)
*   `google-api-python-client` (YouTube Data API)
*   `youtube-transcript-api` (YouTube transcription)
*   `Biopython` (PubMed API)
*   `DuckDuckGoSearch` (DuckDuckGo Search API)
*   `Beautiful Soup` or `Scrapy` (web scraping)
*   `nltk` or `spaCy` (natural language processing)
*   `transformers` (text summarization and generation)
*   Hugo (blog post formatting)
*   n8n (workflow automation)

### F. Next Steps

1.  **Complete the implementation of the YouTube Account Sub-Agent:** Implement the transcription and data storage functionality.
2.  **Implement the YouTube General Search Sub-Agent:** Implement the search, transcription, and data storage functionality.
3.  **Implement the PubMed Sub-Agent:** Implement the search, extraction, and data storage functionality.
4.  **Implement the Web Search Sub-Agent:** Implement the search, scraping, and data storage functionality.
5.  **Implement the Data Synthesis Sub-Agent:** Implement the data analysis, summarization, viewpoint identification, protocol generation, and TLDR summary functionality.
6.  **Implement the Blog Post Generation Sub-Agent:** Implement the blog post outline generation, content writing, linking, embedding, and SEO optimization functionality.
7.  **Integrate with n8n:** Create an n8n workflow to automate the entire process.

This documentation provides a comprehensive overview of the website and the research agent, including the current state, the plan for future development, and the steps required to complete it.