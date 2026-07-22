# Build brief: Hernán Larrea personal portfolio

Build a static personal portfolio website using Python and Pelican. The site will be hosted from the `hjlarrea/hjlarrea.github.io` repository and published at `https://larrea.com.ar`.

The website is Hernán Larrea’s professional home. It should present his positioning, selected work, experience, approach to product and technology, and links to his other identities and projects.

Do not turn this into a blog. Articles, experiments and videos belong to ColoLabs and should only be referenced from this site.

## 1. Brand architecture

Use these identity boundaries throughout the website:

* `larrea.com.ar`: Hernán Larrea’s professional profile and portfolio.
* `cololabs.com.ar`: writing, videos, experiments and creative exploration.
* Independent products such as Arma tu Semana, Repartija and SpotyJam: standalone products created by Hernán.
* LinkedIn: professional network and employment history.
* GitHub: source code and technical activity.

The personal site should be the canonical answer to:

1. Who is Hernán?
2. What kinds of problems does he solve?
3. What evidence demonstrates his capabilities?
4. How can someone contact him?

## 2. Technical stack

Use:

* Python 3
* Latest stable Pelican release
* Jinja2 templates
* Markdown for page and portfolio content
* Plain CSS
* Minimal vanilla JavaScript only where genuinely useful
* GitHub Actions for build and deployment
* GitHub Pages for hosting

Do not introduce:

* React, Vue or another frontend framework
* Tailwind CSS
* A CMS or database
* Server-side rendering
* A JavaScript build chain unless strictly necessary
* A third-party Pelican theme that dictates the visual identity

Create a custom Pelican theme inside the repository.

## 3. Repository structure

Use a structure similar to:

```text
hjlarrea.github.io/
├── content/
│   ├── pages/
│   │   ├── about.md
│   │   ├── work.md
│   │   └── contact.md
│   └── projects/
│       ├── platform-orchestration.md
│       ├── ownership-registry.md
│       ├── monitoring-modernization.md
│       ├── arma-tu-semana.md
│       ├── repartija.md
│       └── spotyjam.md
├── theme/
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── page.html
│   │   ├── work.html
│   │   ├── project.html
│   │   └── includes/
│   │       ├── header.html
│   │       ├── footer.html
│   │       ├── project-card.html
│   │       └── social-links.html
│   └── static/
│       ├── css/
│       │   └── main.css
│       ├── js/
│       │   └── main.js
│       ├── images/
│       └── fonts/
├── plugins/
│   └── portfolio.py
├── output/
├── pelicanconf.py
├── publishconf.py
├── requirements.txt
├── Makefile
├── README.md
├── CNAME
└── .github/
    └── workflows/
        └── deploy.yml
```

If custom Pelican content handling is needed for projects, implement a small local plugin or use a clean metadata convention. Avoid unnecessary plugin dependencies.

The generated `output/` directory should not be committed when GitHub Actions deploys the built artifact.

## 4. Pelican configuration

Development configuration:

```python
AUTHOR = "Hernán Larrea"
SITENAME = "Hernán Larrea"
SITEURL = ""

PATH = "content"
THEME = "theme"

TIMEZONE = "America/Argentina/Buenos_Aires"
DEFAULT_LANG = "en"

RELATIVE_URLS = True

ARTICLE_PATHS = []
PAGE_PATHS = ["pages", "projects"]

STATIC_PATHS = ["images"]

DIRECT_TEMPLATES = ["index"]
```

Production configuration should include:

```python
SITEURL = "https://larrea.com.ar"
RELATIVE_URLS = False
DELETE_OUTPUT_DIRECTORY = True
```

Configure clean URLs where practical. Ensure canonical URLs, Open Graph metadata, a sitemap, favicon support and a useful default social preview.

Include a root-level `CNAME` containing:

```text
larrea.com.ar
```

Ensure that it is copied into the generated GitHub Pages artifact.

## 5. Information architecture

Primary navigation:

```text
Home
Work
About
Contact
```

External links to GitHub and LinkedIn should be visible but secondary to the site navigation.

Do not embed LinkedIn. Link to it directly.

### Routes

```text
/                   Homepage
/work/              Selected work
/work/<project>/    Individual case study
/about/             Professional background and principles
/contact/           Contact information
```

A downloadable CV can be added later. Prepare the navigation and layout so it can be introduced without restructuring the site.

## 6. Homepage

Keep the homepage focused and relatively short.

### Hero

Use this primary positioning:

> I build products and platforms that make complex technology easier to use.

Supporting text:

> I’m Hernán Larrea, a Technical Product Manager with a hands-on background in infrastructure, platform engineering and developer experience.

Primary action:

> View selected work

Secondary action:

> Get in touch

Also provide discreet links to GitHub and LinkedIn.

### Selected work

Show four featured items, with a balance between professional work and independent products:

1. Platform Orchestration
2. Ownership Registry
3. Monitoring and Alerting Modernization
4. Arma tu Semana

Each card should show:

* Project title
* Category
* One-sentence problem or outcome
* Hernán’s role
* Link to the full case study

Do not use technology logos as the primary visual representation.

### Areas of expertise

Use problem-oriented areas:

* Technical product strategy
* Platform engineering and developer experience
* Infrastructure automation
* Internal tools and workflow orchestration
* Product discovery and simplification
* AI-assisted product development

Technologies can appear as supporting context, not as the main message.

### Profile preview

Use:

> I work at the intersection of product strategy and infrastructure. My focus is turning complex technical processes into understandable, usable products that help teams move faster without hiding the operational reality beneath them.

Link to the About page.

### Working principles

Include four short principles:

> Platforms should reduce cognitive load.

> Internal tools are products and should be designed around real user journeys.

> Automation needs visibility, feedback and escape hatches.

> Technology should create leverage without creating unnecessary dependency.

### ColoLabs section

Introduce the separate editorial identity:

> From ColoLabs

> Articles, videos and experiments about technology, products and ideas.

Show up to three manually curated items. Each item must link to its canonical page on `cololabs.com.ar`.

Include:

> ColoLabs is the creative lab of Hernán Larrea.

Do not duplicate complete articles on this website.

### Contact callout

Use:

> Interested in technical product strategy, platform engineering or developer experience? Let’s talk.

Link to the Contact page and `mailto:hernan@larrea.com.ar`.

## 7. Work page

Separate work into two sections.

### Professional case studies

Initially include:

* Platform Orchestration
* Ownership Registry
* Monitoring and Alerting Modernization

These may describe confidential company work. Avoid confidential names, internal details and unsupported performance claims. The case studies can be anonymized while preserving the problem, reasoning and outcome.

### Independent products

Initially include:

* Arma tu Semana
* Repartija
* SpotyJam

Each project should use the same case-study structure:

```text
Overview
Problem
Context
My role
Constraints
Approach
Key decisions
Outcome
What I learned
Related links
```

Do not fabricate metrics, dates, employers, testimonials or outcomes. If information is unavailable, insert a clearly marked content placeholder such as:

```text
[CONTENT NEEDED: Describe the measurable or observable outcome.]
```

The site should still render placeholders gracefully and make them easy to find in the source.

## 8. Project metadata

Use consistent front matter for project files:

```yaml
---
title: Ownership Registry
slug: ownership-registry
category: Professional case study
summary: Making ownership of services and technical resources discoverable.
role: Product strategy and technical design
featured: true
featured_order: 2
status: Case study
external_url:
repository_url:
image:
---
```

Additional optional fields:

```yaml
year:
technologies:
product_areas:
confidential: true
draft: false
```

Create reusable template logic for project cards and project detail pages.

## 9. Initial project summaries

Use these as starting copy, but keep the longer case studies editable in Markdown.

### Platform Orchestration

> A product approach to simplifying complex infrastructure and deployment workflows without creating another disconnected engineering standard.

Areas:

* Platform engineering
* Developer experience
* Workflow orchestration
* Product strategy

### Ownership Registry

> A lightweight, API-first system for answering who owns a service, repository, Kubernetes namespace or Jira project.

Areas:

* Internal tools
* Service ownership
* Platform clarity
* Product discovery

### Monitoring and Alerting Modernization

> Reassessing an inherited alerting system to reduce ignored notifications and route actionable signals into the workflows teams actually use.

Areas:

* Observability
* Operational workflows
* Alert quality
* Platform operations

### Arma tu Semana

> A simple, browser-based weekly planner designed to let people start planning without accounts or unnecessary setup.

Areas:

* Independent product
* Product design
* Self-hosting
* Frictionless onboarding

### Repartija

> A Spanish-language expense-sharing application designed to make splitting the cost of gatherings simple and understandable.

Areas:

* Independent product
* API design
* Responsive web
* User experience

### SpotyJam

> A collaborative playlist experience where guests can suggest songs anonymously without needing a Spotify account.

Areas:

* Independent product
* Spotify integration
* Social experience
* Product experimentation

## 10. About page

The About page should tell a concise professional story, not reproduce a résumé.

Start with:

> I’m a Technical Product Manager with a background in infrastructure engineering. I work where product strategy, platform engineering and developer experience meet.

Continue by explaining that Hernán:

* Remains technically hands-on
* Approaches platforms as products and force multipliers
* Focuses on reducing friction and cognitive load
* Connects technical constraints with user and organizational needs
* Builds independent products and experiments outside his professional work
* Uses ColoLabs to publish ideas, tutorials, videos and experiments

Include a section titled “How I work” covering:

* Begin with the workflow and user problem
* Question whether another abstraction is actually necessary
* Prefer incremental enablement over large platform rewrites
* Treat feedback and observability as part of the experience
* Use prototypes to clarify decisions

End with links to Work, ColoLabs, GitHub and LinkedIn.

## 11. ColoLabs curation

Do not create separate Writing or Uses pages. Selected external work should appear only in the homepage “From ColoLabs” section.

Each item should support:

```yaml
title:
summary:
type: Article | Video | Experiment
url:
date:
topics:
featured:
```

Start with content stored in a local data file, such as:

```text
data/cololabs.yml
```

Do not implement automatic RSS ingestion initially. Keep the implementation deterministic and easy to maintain. Leave a brief note in the README explaining how RSS ingestion could be added later.

## 13. Contact page

Include:

* Email: `hernan@larrea.com.ar`
* GitHub: `https://github.com/hjlarrea`
* LinkedIn: `https://linkedin.com/in/hjlarrea`
* ColoLabs: `https://cololabs.com.ar`

Do not add a contact form because GitHub Pages has no native backend and the form is not needed for the first version.

## 14. Visual direction

The design should feel:

* Minimal
* Technical but not visually cold
* Professional without looking corporate
* Editorial rather than dashboard-like
* Confident, understated and readable

Use generous whitespace, clear typography and restrained color.

Suggested starting tokens:

```css
:root {
  --color-background: #f7f6f2;
  --color-surface: #ffffff;
  --color-text: #171717;
  --color-muted: #686868;
  --color-border: #dcdad3;
  --color-accent: #ff6500;
  --color-accent-hover: #b84200;

  --font-body: Inter, system-ui, sans-serif;
  --font-display: "Space Grotesk", Inter, system-ui, sans-serif;

  --content-width: 72rem;
  --reading-width: 46rem;
  --radius-small: 0.35rem;
  --radius-medium: 0.75rem;
}
```

Use local or system fonts where possible. If external font hosting is used, ensure the site still looks acceptable when it fails.

Avoid:

* Excessive gradients
* Animated backgrounds
* Glassmorphism
* Skill progress bars
* Stock photography
* Generic technology-logo grids
* Large amounts of motion
* A dark terminal aesthetic as the entire identity

A dark mode is optional, not an MVP requirement.

## 15. Responsive and accessible behavior

The site must:

* Work from approximately 320px width upward
* Use semantic HTML
* Support keyboard navigation
* Have visible focus states
* Meet WCAG AA color contrast
* Respect `prefers-reduced-motion`
* Use useful alternative text
* Have correctly nested headings
* Avoid layout shifts caused by images or fonts
* Provide a skip-to-content link

The navigation should collapse cleanly on mobile. Use minimal JavaScript for the mobile menu, or implement it using semantic HTML if practical.

## 16. SEO and metadata

Implement:

* Unique title and description for every page
* Canonical URLs
* Open Graph metadata
* Twitter/X card metadata
* `sitemap.xml`
* `robots.txt`
* Favicon
* Social preview image support
* JSON-LD `Person` schema on the homepage

The `Person` schema can reference:

* Hernán Larrea
* `larrea.com.ar`
* GitHub
* LinkedIn
* ColoLabs

Do not add employers, job history or other structured data that has not been explicitly provided.

## 17. GitHub Actions deployment

Create a GitHub Actions workflow that:

1. Checks out the repository.
2. Sets up Python.
3. Installs dependencies from `requirements.txt`.
4. Builds using `publishconf.py`.
5. Uploads the generated `output/` directory as the Pages artifact.
6. Deploys using GitHub’s official Pages actions.

Run on:

* Pushes to `main`
* Manual workflow dispatch

Use GitHub’s current official Pages actions and pin them to stable major versions.

The workflow should request only the permissions it needs:

```yaml
permissions:
  contents: read
  pages: write
  id-token: write
```

## 18. Local development

Provide simple commands:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pelican --listen --autoreload
```

Also provide:

```bash
make dev
make build
make publish
```

Document these commands in the README.

## 19. Acceptance criteria

The implementation is complete when:

* The entire site builds successfully from a clean environment.
* GitHub Actions can deploy the generated site.
* All primary routes work with clean internal links.
* The homepage includes positioning, featured work, expertise, principles, ColoLabs and contact sections.
* Project pages are generated consistently from Markdown.
* No fabricated personal or project information is present.
* Missing content is marked clearly in source files.
* The site works on mobile and desktop.
* Keyboard navigation and focus states work.
* Production URLs use `https://larrea.com.ar`.
* The generated artifact includes the `CNAME`.
* There are no JavaScript console errors.
* The README explains editing content, adding a project, curating ColoLabs links and deploying the site.

## 20. Implementation approach

First inspect the existing repository and preserve useful content or configuration. Do not overwrite existing work blindly.

Then:

1. Establish the Pelican configuration and custom theme.
2. Build shared layout, navigation and footer components.
3. Implement homepage and standard content pages.
4. Add the portfolio content model and case-study templates.
5. Add the initial project content.
6. Implement metadata, accessibility and responsive behavior.
7. Add deployment automation.
8. Run the production build and inspect the generated HTML.
9. Report any remaining content placeholders.

Favor a polished, maintainable first version over extra features. The objective is a credible professional portfolio, not a demonstration of frontend complexity.
