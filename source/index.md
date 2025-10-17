# DocCraft Toolkit

## Introduction

This comprehensive reference demonstrates **MyST-Parser** and **Sphinx** capabilities for creating professional technical documentation. MyST (Markedly Structured Text) extends Markdown with powerful features for scientific and technical writing.

This toolkit includes:
- **Advanced Markdown syntax** with MyST extensions
- **Interactive Sphinx-Design components** for modern UIs  
- **Mathematical expressions** with LaTeX/MathJax support
- **Comprehensive diagram support** with lot of Mermaid types
- **Professional publishing** with HTML and PDF output

```{note}
**Target Audience:** Technical writers, researchers, software developers, and documentation teams building sophisticated documentation systems.
```

See also [MyST Parser Documentation](https://myst-parser.readthedocs.io/) and [Sphinx Documentation](https://www.sphinx-doc.org/).

## Figures and Images

MyST-Parser provides advanced image and figure handling with captions, references, and flexible layouts.

### Basic Figure with Caption

Figures include captions and can be referenced throughout the document:

```{figure} _static/img/sample.png
:alt: Sample Figure
:align: center
:width: 400px
:name: sample-figure

Sample figure demonstrating image inclusion with proper captioning and alignment
```

You can reference figures in your text using the `:name:` attribute. For example, see {numref}`sample-figure` above.

### Inline Images

Small images can be embedded inline with text wrapping:

```{image} _static/img/sample.png
:alt: Small inline
:width: 70px
:align: left
```

This text flows around the small image on the left. Images can be sized using various units like pixels, percentages, or relative units. that could be useful for small and minor images in some contexts.

### Full-Width Images

Images can span the entire content width for maximum visual impact:

```{image} _static/img/sample.png
:alt: Full width image
:width: 100%
:align: center
```

## Sphinx-Design Components

Sphinx-Design provides modern, responsive web components for documentation.

### Cards

:::::{grid} 1 1 2 3
:class-container: text-center
:gutter: 3

::::{grid-item-card}
:link: https://example.com
:shadow: md

**Feature Card**
^^^
This is a clickable card with a shadow effect. Cards are great for organizing content into digestible sections.
+++
Explore more →
::::

::::{grid-item-card}
:shadow: md

**Info Card**
^^^
Cards can contain any content including images, code blocks, and formatted text.
+++
Learn More
::::

::::{grid-item-card}
:shadow: md

**Action Card**
^^^
Use cards to highlight important features, calls-to-action, or key information points.
+++
Get Started
::::
:::::

### Dropdowns and Details

```{dropdown} Click to expand
:animate: fade-in-slide-down

This content is hidden by default and reveals when clicked. Perfect for:
- FAQ sections
- Optional advanced information
- Code examples that might clutter the main text
- Additional details that some users might want to skip
```

````{dropdown} Advanced Configuration
:class-title: sd-bg-primary sd-text-white
:animate: fade-in-slide-down

This is a styled dropdown block. You can customize:

- Background colors
- Icons
- Animation effects
- Collapsible behavior

```python
# Example configuration
config = {
    "theme": "modern",
    "responsive": True,
    "animations": "enabled"
}
```
````

### Buttons and Badges

```{button-link} https://example.com
:color: primary
:shadow:

Primary Button
```

```{button-ref} sample-figure
:ref-type: ref
:color: secondary
:outline:

Reference Button
```

**Badges:**
{bdg}`Default`
{bdg-primary}`Primary`
{bdg-secondary}`Secondary`
{bdg-success}`Success`
{bdg-info}`Info`
{bdg-warning}`Warning`
{bdg-danger}`Danger`
{bdg-light}`Light`
{bdg-dark}`Dark`

### Tabs

````{tab-set}

```{tab-item} Python
:sync: python

```python
def hello_world():
    print("Hello from Python!")
    return "Success"
```

```{tab-item} JavaScript
:sync: js

```javascript
function helloWorld() {
    console.log("Hello from JavaScript!");
    return "Success";
}
```

```{tab-item} Shell
:sync: shell

```bash
echo "Hello from Shell!"
```

````

### Admonitions

```{note}
This is a note admonition. Use it for helpful information that supplements the main content.
```

```{tip}
**Pro Tip:** Admonitions draw attention to important information and improve content scanability.
```

```{warning}
**Important:** This is a warning about potential issues or important considerations.
```

```{danger}
**Critical:** This indicates something that could cause serious problems if ignored.
```

```{seealso}
**Related Topics:**
- [Markdown Guide](https://www.markdownguide.org/)
- [MyST Parser Documentation](https://myst-parser.readthedocs.io/)
- [Sphinx-Design Documentation](https://sphinx-design.readthedocs.io/)
```

### Synchronized Tabs

Content can be synchronized across tab sets using the `:sync:` option.

````{tab-set}

```{tab-item} Config
:sync: config-example

```yaml
# config.yaml
database:
  host: localhost
  port: 5432
  name: myapp
```

```{tab-item} Environment
:sync: env-example

```bash
# .env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=myapp
```

````

````{tab-set}

```{tab-item} Python Implementation
:sync: config-example

```python
# Using the YAML config
import yaml

with open('config.yaml') as f:
    config = yaml.safe_load(f)

db_url = f"postgresql://{config['database']['host']}:{config['database']['port']}/{config['database']['name']}"
```

```{tab-item} Environment Variables
:sync: env-example

```python
# Using environment variables
import os

db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')

db_url = f"postgresql://{db_host}:{db_port}/{db_name}"
```

````

### Grid Layouts

::::{grid} 2
:gutter: 2

:::{grid-item}
**Left Column**

This demonstrates a two-column layout using the grid system. Perfect for:

- Comparison content
- Before/after examples
- Side-by-side code and explanation
  :::

:::{grid-item}
**Right Column**

Grids are responsive and will stack on smaller screens. You can specify different column counts for different screen sizes.
:::
::::

## Lists

Markdown supports several types of lists for organizing content hierarchically.

### Unordered Lists

Bullet points are perfect for items without a specific order or priority:

- First item
- Second item
  - Nested item 1
  - Nested item 2
    - Deeply nested item
- Third item

### Ordered Lists

Numbered lists work well for step-by-step instructions or ranked items:

1. First step
1. Second step
   1. Sub-step A
   1. Sub-step B
1. Third step

### Task Lists

Interactive checkboxes are excellent for tracking progress and todo items:

- [x] Completed task
- [x] Another completed task
- [ ] Pending task
- [ ] Another pending task

## Code Examples

Code blocks and syntax highlighting make technical documentation clear and readable.

### Inline Code

Use backticks for short code snippets within text. For example: Use the `print()` function to display output in Python.

### Code Blocks

Python syntax highlighting with line numbers and proper indentation:

```python
def fibonacci(n):
    """Generate Fibonacci sequence up to n terms."""
    fib_sequence = [0, 1]

    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])

    return fib_sequence[:n]

# Generate first 10 Fibonacci numbers
result = fibonacci(10)
print(f"Fibonacci sequence: {result}")
```

JavaScript with async/await patterns and error handling:

```javascript
// Async function to fetch data
async function fetchUserData(userId) {
  try {
    const response = await fetch(`/api/users/${userId}`);
    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error fetching user data:", error);
    throw error;
  }
}
```

Database queries with proper formatting and joins:

```sql
SELECT
    u.user_id,
    u.username,
    COUNT(o.order_id) as total_orders,
    SUM(o.total_amount) as total_spent
FROM users u
LEFT JOIN orders o ON u.user_id = o.user_id
WHERE u.created_at >= '2024-01-01'
GROUP BY u.user_id, u.username
HAVING COUNT(o.order_id) > 5
ORDER BY total_spent DESC;
```

## Mathematical Expressions

MyST-Parser supports LaTeX-style mathematical notation using MathJax for both inline and display equations.

### Inline Mathematics

Mathematical expressions can be embedded within text using single dollar signs: The quadratic formula is $ax^2 + bx + c = 0$ and its solution is $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$.

### Display Mathematics

Complex equations are better presented as centered display blocks using double dollar signs:

$$
E = mc^2
$$

$$
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
$$

### Mathematical Environments

Advanced mathematical structures using LaTeX environments:

$$
\nabla \times \vec{\mathbf{B}} -\, \frac{1}{c}\, \frac{\partial\vec{\mathbf{E}}}{\partial t} = \frac{4\pi}{c}\vec{\mathbf{j}}
$$

$$
\nabla \cdot \vec{\mathbf{E}} = 4 \pi \rho
$$

$$
\nabla \times \vec{\mathbf{E}}\, +\, \frac{1}{c}\, \frac{\partial\vec{\mathbf{B}}}{\partial t} = \vec{\mathbf{0}}
$$

$$
\nabla \cdot \vec{\mathbf{B}} = 0
$$

### Matrices and Arrays

Linear algebra expressions with matrices:

$$
\begin{pmatrix}
a & b \\
c & d
\end{pmatrix}
\begin{pmatrix}
x \\
y
\end{pmatrix} = 
\begin{pmatrix}
ax + by \\
cx + dy
\end{pmatrix}
$$

### Mathematical Notation Examples

Common mathematical symbols and operators:

- **Greek letters**: $\alpha$, $\beta$, $\gamma$, $\Delta$, $\Omega$
- **Calculus**: $\frac{d}{dx}$, $\int$, $\sum_{i=1}^{n}$, $\prod_{i=1}^{n}$
- **Logic**: $\forall$, $\exists$, $\land$, $\lor$, $\neg$
- **Set theory**: $\in$, $\subset$, $\cup$, $\cap$, $\emptyset$
- **Arrows**: $\rightarrow$, $\Rightarrow$, $\leftrightarrow$, $\Leftrightarrow$

### Complex Equations

Advanced mathematical expressions for scientific documentation:

$$
\frac{\partial^2 u}{\partial t^2} = c^2 \nabla^2 u = c^2 \left( \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} + \frac{\partial^2 u}{\partial z^2} \right)
$$

$$
\mathcal{L} = \frac{1}{2} m \dot{q}^2 - V(q) = T - V
$$

### Chemical Equations

Chemical formulas and reactions:

$$
\text{H}_2\text{O} + \text{CO}_2 \rightleftharpoons \text{H}_2\text{CO}_3
$$

$$
\text{CaCO}_3 \xrightarrow{\Delta} \text{CaO} + \text{CO}_2 \uparrow
$$

## Tables and Data Presentation

MyST supports enhanced table formatting with captions, references, and styling options.

### Basic Tables with Captions

Tables can be numbered, referenced, and given descriptive captions:

```{table} Employee Information
:name: employee-table

| Name    | Age | City          | Occupation |
| ------- | --- | ------------- | ---------- |
| Alice   | 28  | New York      | Engineer   |
| Bob     | 35  | San Francisco | Designer   |
| Charlie | 42  | Seattle       | Manager    |
| Diana   | 31  | Boston        | Developer  |
```

```{table} Text Alignment Examples
:name: alignment-table

| Left Aligned | Center Aligned | Right Aligned |
| :----------- | :------------: | ------------: |
| Text         |      Text      |          Text |
| More text    |   More text    |     More text |
| $10.00       |     $20.00     |        $30.00 |
```

```{table} Quarterly Sales Data
:name: sales-table

| Product   | Q1 Sales    | Q2 Sales    | Q3 Sales    | Q4 Sales    | Total        |
| --------- | ----------- | ----------- | ----------- | ----------- | ------------ |
| Widget A  | $15,000     | $18,000     | $22,000     | $25,000     | $80,000      |
| Widget B  | $12,000     | $14,000     | $16,000     | $18,000     | $60,000      |
| Widget C  | $20,000     | $22,000     | $24,000     | $28,000     | $94,000      |
| **Total** | **$47,000** | **$54,000** | **$62,000** | **$71,000** | **$234,000** |
```

### Advanced Table Features

Tables can reference other elements and include mathematical expressions. For example, see the performance data in {numref}`sales-table` which correlates with the metrics shown in our XY scatter plots in the diagrams section.

## Diagrams

Mermaid diagrams provide powerful visualization capabilities for technical documentation.

### Flowcharts

Flowcharts visualize decision processes and workflow logic:

```{mermaid}
:caption: Debugging workflow flowchart showing the iterative process of testing, debugging, and fixing issues

flowchart TD
    A[Start] --> B{Is it working?}
    B -->|Yes| C[Great!]
    B -->|No| D[Debug]
    D --> E{Found the issue?}
    E -->|Yes| F[Fix it]
    E -->|No| G[Google it]
    G --> D
    F --> H[Test]
    H --> B
    C --> I[End]
```

### Sequence Diagrams

Sequence diagrams show interactions between different actors over time:

```{mermaid}
:caption: User authentication sequence showing the login process flow between user, browser, server, and database

sequenceDiagram
    participant User
    participant Browser
    participant Server
    participant Database

    User->>Browser: Enter credentials
    Browser->>Server: POST /login
    Server->>Database: Query user
    Database-->>Server: Return user data
    Server->>Server: Validate credentials
    alt Credentials valid
        Server-->>Browser: Return JWT token
        Browser-->>User: Show dashboard
    else Credentials invalid
        Server-->>Browser: Return error
        Browser-->>User: Show error message
    end
```

### Entity Relationship Diagrams (ERD)

ERDs model database structures and relationships between entities:

```{mermaid}
:caption: E-commerce database entity relationship diagram showing relationships between customers, orders, products, and line items

erDiagram
    CUSTOMER ||--o{ ORDER : places
    ORDER ||--|{ LINE-ITEM : contains
    CUSTOMER }|..|{ DELIVERY-ADDRESS : uses
    PRODUCT ||--o{ LINE-ITEM : includes

    CUSTOMER {
        int customer_id PK
        string name
        string email
        date created_at
    }

    ORDER {
        int order_id PK
        int customer_id FK
        date order_date
        decimal total_amount
        string status
    }

    PRODUCT {
        int product_id PK
        string name
        decimal price
        int stock_quantity
    }

    LINE-ITEM {
        int line_item_id PK
        int order_id FK
        int product_id FK
        int quantity
        decimal unit_price
    }
```

### Gantt Charts

Project timeline visualization with phases and dependencies:

```{mermaid}
:caption: Project development timeline showing phases from planning through deployment

gantt
    title Project Timeline
    dateFormat YYYY-MM-DD
    section Planning
    Requirements gathering    :2024-01-01, 14d
    Design phase             :2024-01-15, 21d
    section Development
    Backend development      :2024-02-05, 30d
    Frontend development     :2024-02-15, 25d
    section Testing
    Integration testing      :2024-03-07, 14d
    User acceptance testing  :2024-03-21, 10d
    section Deployment
    Production deployment    :2024-04-01, 5d
```

### Pie Charts

Statistical data visualization for showing proportions:

```{mermaid}
:caption: Market share distribution across different product categories

pie title Market Share by Product
    "Product A" : 35
    "Product B" : 25
    "Product C" : 20
    "Product D" : 15
    "Others" : 5
```

### User Journey Diagrams

Map user experiences and emotional states throughout a process:

```{mermaid}
:caption: Software developer's debugging journey showing the emotional rollercoaster of finding bugs

journey
    title The Great Bug Hunt
    section Discovery
      Found mysterious bug: 5: Developer
      Coffee consumed: 4: Developer
      Stack Overflow searched: 3: Developer
    section Resolution
      "Quick fix" attempted: 2: Developer
      Entire system breaks: 1: Developer
      Realizes typo in variable name: 0: Developer
```

### State Diagrams

Model state machines and transitions in system behavior:

```{mermaid}
:caption: Document workflow state diagram showing the lifecycle from draft to publication or rejection

stateDiagram-v2
    [*] --> Draft
    Draft --> InReview: Submit
    InReview --> Draft: Request Changes
    InReview --> Approved: Approve
    InReview --> Rejected: Reject
    Approved --> Published: Publish
    Published --> Archived: Archive
    Archived --> [*]
    Rejected --> [*]
```

### Component Architecture Diagrams

System architecture visualization with layered components:

```{mermaid}
:caption: Component diagram showing the architecture of a web application system

flowchart TB
    subgraph "Frontend Layer"
        UI[User Interface]
        Router[Router Component]
        Auth[Authentication Component]
    end

    subgraph "Backend Layer"
        API[REST API Gateway]
        AuthService[Authentication Service]
        UserService[User Service]
        OrderService[Order Service]
        ProductService[Product Service]
    end

    subgraph "Data Layer"
        UserDB[(User Database)]
        ProductDB[(Product Database)]
        OrderDB[(Order Database)]
        Cache[(Redis Cache)]
    end

    subgraph "External Services"
        PaymentGW[Payment Gateway]
        EmailService[Email Service]
        Logger[Logging Service]
    end

    UI --> Router
    Router --> Auth
    Auth --> API
    API --> AuthService
    API --> UserService
    API --> OrderService
    API --> ProductService

    AuthService --> UserDB
    UserService --> UserDB
    OrderService --> OrderDB
    ProductService --> ProductDB

    OrderService --> PaymentGW
    OrderService --> EmailService
    API --> Cache
    API --> Logger
```

### UML Class Diagrams

Object-oriented design with inheritance and relationships:

```{mermaid}
:caption: UML class diagram showing object-oriented system structure with inheritance and relationships

classDiagram
    class Animal {
        +String name
        +int age
        +makeSound()
        +move()
    }

    class Dog {
        +String breed
        +bark()
        +wagTail()
    }

    class Cat {
        +String color
        +meow()
        +purr()
    }

    class Owner {
        +String name
        +String address
        +feedPet()
        +walkPet()
    }

    Animal <|-- Dog
    Animal <|-- Cat
    Owner "1" --> "*" Animal : owns
```

### Mind Maps

Hierarchical organization of ideas and concepts:

```{mermaid}
:caption: Project planning mindmap showing main components and their subcategories

mindmap
  root((Project Planning))
    Requirements
      Functional
        User Stories
        Use Cases
      Non-Functional
        Performance
        Security
        Scalability
    Design
      Architecture
        Frontend
        Backend
        Database
      UI/UX
        Wireframes
        Prototypes
    Development
      Frontend
        React Components
        State Management
      Backend
        API Endpoints
        Business Logic
      Testing
        Unit Tests
        Integration Tests
    Deployment
      CI/CD Pipeline
      Production Environment
      Monitoring
```

### Timeline Diagrams

Chronological visualization of events and milestones:

```{mermaid}
:caption: Software development project timeline showing major milestones and deliverables

timeline
    title Software Development Timeline

    2024-01 : Project Kickoff
           : Requirements Gathering
           : Team Assembly

    2024-02 : System Design
           : Architecture Planning
           : Technology Selection

    2024-03 : Development Phase 1
           : Core Features
           : Database Setup

    2024-04 : Development Phase 2
           : User Interface
           : API Integration

    2024-05 : Testing & QA
           : User Acceptance Testing
           : Performance Optimization

    2024-06 : Production Deployment
           : Go-Live
           : Post-Launch Support
```

### Quadrant Charts

Two-dimensional categorization for decision-making matrices:

```{mermaid}
:caption: Feature priority matrix showing importance vs effort quadrants for project planning

quadrantChart
    title Feature Priority Matrix
    x-axis Low Effort --> High Effort
    y-axis Low Impact --> High Impact

    quadrant-1 Quick Wins
    quadrant-2 Major Projects
    quadrant-3 Fill-ins
    quadrant-4 Thankless Tasks

    User Authentication: [0.8, 0.9]
    Dashboard: [0.7, 0.8]
    Email Notifications: [0.3, 0.7]
    Advanced Analytics: [0.9, 0.6]
    Dark Mode: [0.2, 0.4]
    Mobile App: [0.9, 0.9]
    API Documentation: [0.4, 0.3]
    Performance Monitoring: [0.6, 0.8]
```

### Sankey Flow Diagrams

Flow visualization showing quantities moving between nodes:

```{mermaid}
:caption: Energy flow diagram showing renewable energy distribution across different sectors

sankey-beta

    Solar,Residential,15
    Solar,Commercial,25
    Solar,Industrial,10

    Wind,Residential,20
    Wind,Commercial,35
    Wind,Industrial,25

    Hydro,Residential,10
    Hydro,Commercial,15
    Hydro,Industrial,20

    Residential,Heating,25
    Residential,Lighting,15
    Residential,Appliances,15

    Commercial,HVAC,40
    Commercial,Lighting,20
    Commercial,Equipment,15

    Industrial,Manufacturing,35
    Industrial,Processing,20
```

### XY Scatter Plots

Coordinate-based data visualization for correlation analysis:

```{mermaid}
:caption: Performance metrics scatter plot showing response time vs throughput correlation

xychart-beta
    title "API Performance Metrics"
    x-axis "Response Time (ms)" 0 --> 1000
    y-axis "Throughput (req/s)" 0 --> 500

    line [100, 450, 150, 400, 200, 350, 250, 300, 300, 250]
    line [200, 350, 250, 320, 300, 280, 350, 240, 400, 200]
    line [50, 300, 100, 280, 150, 260, 200, 240, 250, 220]
```

### Block Diagrams

High-level system architecture with component relationships:

```{mermaid}
:caption: High-level system architecture showing main components and data flow

block-beta
    columns 3

    Frontend["Frontend App"]
    API["API Gateway"]
    Auth["Auth Service"]

    space
    LoadBalancer["Load Balancer"]
    space

    Database[("Database")]
    Cache[("Redis Cache")]
    Queue[("Message Queue")]

    Frontend --> API
    API --> Auth
    API --> LoadBalancer
    LoadBalancer --> Database
    LoadBalancer --> Cache
    API --> Queue
```

### Cloud Architecture Diagrams

Modern infrastructure visualization with services and connections:

```{mermaid}
:caption: Cloud infrastructure architecture showing services and their connections

architecture-beta
    group api(cloud)[API Services]
    group frontend(cloud)[Frontend]
    group external(cloud)[External Services]

    service db(database)[Database] in api
    service auth(server)[Auth Service] in api
    service gateway(internet)[API Gateway] in api

    service web(server)[Web App] in frontend
    service cdn(disk)[CDN] in frontend

    service payment(server)[Payment Gateway] in external
    service email(server)[Email Service] in external

    web:R -- L:gateway
    gateway:R -- L:auth
    gateway:B -- T:db
    auth:R -- L:payment
    gateway:T -- B:email
    cdn:B -- T:web
```

### Kanban Boards

Agile project management workflow visualization:

```{mermaid}
:caption: Agile development workflow showing task progression through different stages

kanban
    Backlog
        Bug Fix #123
        Feature Request #456
        Code Review #789

    In Progress
        User Authentication
        Dashboard Design

    Testing
        Payment Integration
        Email Notifications

    Done
        Project Setup
        Database Schema
        API Documentation
```

### Requirements Traceability Diagrams

System requirements management and relationship tracking:

```{mermaid}
:caption: Requirements traceability showing system requirements and their relationships

requirementDiagram

    requirement user_req {
        id: 1
        text: Users shall be able to login
        risk: high
        verifymethod: test
    }

    requirement perf_req {
        id: 2
        text: System shall respond within 2 seconds
        risk: medium
        verifymethod: test
    }

    requirement sec_req {
        id: 3
        text: All data shall be encrypted
        risk: high
        verifymethod: inspection
    }

    functionalRequirement login_func {
        id: 1.1
        text: Login form validation
        risk: low
        verifymethod: test
    }

    performanceRequirement response_time {
        id: 2.1
        text: API response optimization
        risk: medium
        verifymethod: test
    }

    user_req - derives -> login_func
    perf_req - derives -> response_time
    sec_req - satisfies -> login_func
```

## Advanced MyST Features

Professional documentation requires advanced formatting capabilities beyond basic Markdown.

### Cross-References and Citations

MyST enables sophisticated cross-referencing throughout documents:

- **Figure references**: {numref}`sample-figure` demonstrates image handling
- **Table references**: See {numref}`employee-table` for data examples  
- **Section references**: Mathematical expressions are covered in the Mathematical Expressions section
- **External links**: [MyST Documentation](https://myst-parser.readthedocs.io/) and [Sphinx Guide](https://www.sphinx-doc.org/)

### Footnotes and Annotations

Footnotes provide supplementary information without disrupting reading flow[^demo-note]:

[^demo-note]: This footnote demonstrates academic-style citations and additional context.

Complex topics often require detailed explanations that would interrupt the main narrative[^technical-note].

[^technical-note]: 
    This extended footnote shows how to handle:
    - Multi-line explanations
    - Technical specifications  
    - Implementation details
    - Reference citations

### Typography and Special Characters

MyST handles advanced typography automatically:

- **Smart quotes**: "Professional typography" with proper quotation marks
- **Em dashes**: Technical writing—like this document—benefits from proper punctuation
- **Mathematical symbols**: Variables like $\alpha$, $\beta$, $\gamma$ integrate seamlessly with text
- **Character escaping**: Use backslashes to escape special characters: \*literal asterisks\*, \[literal brackets\]

### Integration Capabilities

This toolkit demonstrates integration between:

:::::{grid} 2
:gutter: 3

::::{grid-item-card} Data & Analytics
- Mathematical expressions with LaTeX
- Statistical visualizations  
- Research data presentation
- Scientific notation support
::::

::::{grid-item-card} Development Workflows
- Code documentation with syntax highlighting
- API reference generation
- Software architecture diagrams
- Technical specification writing
::::
:::::

## Publication Outputs

This documentation system generates multiple professional outputs:

```{dropdown} **HTML Output Features**
:animate: fade-in-slide-down

- **Responsive design** with mobile optimization
- **Interactive elements** (dropdowns, tabs, buttons)
- **Search functionality** with full-text indexing
- **Theme customization** with CSS and JavaScript
- **Accessibility compliance** with ARIA standards
```

```{dropdown} **PDF Output Features** 
:animate: fade-in-slide-down

- **Professional typesetting** with LaTeX engine
- **High-quality diagrams** with vector graphics
- **Academic formatting** with proper citations
- **Print optimization** with appropriate page breaks
- **Cross-reference links** maintained in PDF
```

```{seealso}
**Essential Resources:**
- [MyST Syntax Reference](https://myst-parser.readthedocs.io/en/latest/syntax/syntax.html)
- [Sphinx-Design Components](https://sphinx-design.readthedocs.io/)
- [Mermaid Diagram Documentation](https://mermaid.js.org/)
- [LaTeX Mathematical Notation](https://en.wikibooks.org/wiki/LaTeX/Mathematics)
```

---

## Conclusion

**DocCraft Toolkit** provides a complete foundation for creating sophisticated technical documentation. The combination of MyST's enhanced Markdown syntax, Sphinx's powerful publishing capabilities, and modern design components enables documentation that meets professional publishing standards.

Whether you're documenting software APIs, writing research papers, creating user manuals, or building knowledge bases, this toolkit provides the features needed for clear, maintainable, and professional documentation.

**Ready to build exceptional documentation!**
