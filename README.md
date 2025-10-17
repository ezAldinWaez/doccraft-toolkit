# DocCraft Toolkit (V0.1)

A comprehensive documentation system built with **Sphinx** and **MyST-Parser** for creating professional technical documentation with modern features.

## Features

- **Advanced Markdown** with MyST extensions
- **Interactive components** using Sphinx-Design
- **Mathematical expressions** with LaTeX/MathJax support
- **20+ Mermaid diagram types** for visualization
- **Professional publishing** to HTML and PDF
- **Responsive design** with mobile optimization

## Quick Start

### Prerequisites

- Python 3.8+
- Node.js

### Installation

```bash
# Install Python dependencies
pip install sphinx myst-parser sphinx-design sphinxcontrib-mermaid

# Install Mermaid CLI for diagram generation
npm install -g @mermaid-js/mermaid-cli

# Install any other necessary dependency
```

### Build Documentation

```bash
# HTML output
make html

# PDF output
make latexpdf

# Clean build files
make clean
```

### View Output

- **HTML**: Open `build/html/index.html` in your browser
- **PDF**: Find generated PDF in `build/latex/`

## Project Structure

```
doccraft-toolkit/
├── source/
│   ├── index.md          # Main documentation content
│   ├── conf.py           # Sphinx configuration
│   └── _static/          # Static assets
├── build/                # Generated outputs
├── Makefile              # Build commands
└── README.md             # README file
```

## Documentation Features

### Diagrams

- Flowcharts, sequence diagrams, ERDs
- Gantt charts, pie charts, mind maps
- Architecture diagrams, class diagrams
- And 15+ more Mermaid types

### Interactive Components

- Collapsible sections and dropdowns
- Tabbed content with synchronization
- Cards, buttons, and badges
- Responsive grid layouts

### Mathematical Content

- Inline and display equations
- LaTeX notation support
- Chemical formulas
- Matrix and vector operations

### Advanced Typography

- Cross-references and citations
- Footnotes and annotations
- Professional table formatting
- Smart quotes and special characters

## Resources

- [MyST Parser Documentation](https://myst-parser.readthedocs.io/)
- [Sphinx Documentation](https://www.sphinx-doc.org/)
- [Sphinx-Design Components](https://sphinx-design.readthedocs.io/)
- [Mermaid Diagram Syntax](https://mermaid.js.org/)

---

**Ready to build exceptional documentation with DocCraft!**