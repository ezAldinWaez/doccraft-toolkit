# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

DocCraft Toolkit is a comprehensive documentation system built with Sphinx and MyST-Parser. It demonstrates advanced technical documentation capabilities including:

- MyST-enhanced Markdown with 20+ extensions
- 20+ Mermaid diagram types (flowcharts, ERDs, Gantt, architecture, etc.)
- Sphinx-Design interactive components (cards, tabs, dropdowns, grids)
- Mathematical expressions with LaTeX/MathJax
- Dual output: responsive HTML and professional PDF

## Common Commands

### Building Documentation

```bash
# HTML output (most common)
make html

# PDF output via LaTeX
make latexpdf

# Clean all build artifacts
make clean

# View available build targets
make help
```

### Development Workflow

```bash
# Quick rebuild after changes
make html

# Full clean rebuild
make clean && make html

# Test PDF generation (requires LaTeX packages)
make latexpdf
```

### Dependencies Installation

```bash
# Core Python dependencies
pip install sphinx myst-parser sphinx-design sphinxcontrib-mermaid

# Mermaid CLI for diagram generation
npm install -g @mermaid-js/mermaid-cli

# Chrome for Puppeteer (if Mermaid fails)
npx puppeteer browsers install chrome
```

## Architecture & File Structure

### Core Configuration

- `source/conf.py` - Central Sphinx configuration with extensions, themes, and LaTeX settings
- `Makefile` - Standard Sphinx makefile for build commands
- `source/index.md` - Main content demonstrating all features (1100+ lines)

### Key Configuration Details

- **Project name extraction**: `conf.py` dynamically reads project name from first line of `index.md`
- **MyST extensions**: 12 extensions enabled including `dollarmath`, `mermaid`, `attrs_block`
- **Mermaid integration**: SVG output with PDF cropping for LaTeX builds
- **LaTeX packages**: Comprehensive math/chemistry support (`amsmath`, `mhchem`, `booktabs`)

### Content Organization

- `source/index.md` - Comprehensive feature showcase and reference
- `source/_static/` - Assets (CSS, images)
- `build/html/` - Generated HTML output
- `build/latex/` - Generated LaTeX/PDF output

## Critical Build Requirements

### LaTeX Considerations

- **Unicode handling**: Avoid Unicode characters in titles (use "and" not "&")
- **Emoji restrictions**: Remove emojis for PDF compatibility
- **Math notation**: Use LaTeX math mode (`$\alpha$`) not Unicode (α)
- **Cross-references**: Use proper MyST syntax, not arbitrary labels

### Mermaid Diagrams

- All 20+ diagram types are implemented and tested
- Beta features (architecture-beta, sankey-beta, xychart-beta) require specific syntax
- Chrome/Puppeteer dependency for rendering
- SVG output preferred for scalability

### MyST-Parser Features

- Figure numbering with `{numref}` references
- Table captions with numbered references
- Sphinx-Design components (grids, cards, tabs, dropdowns)
- Mathematical expressions in both inline and display modes

## Development Notes

### Adding New Content

- Follow MyST syntax shown in `index.md` examples
- Test both HTML and PDF builds before committing
- Use proper figure/table numbering for cross-references
- Maintain consistent heading hierarchy

### Troubleshooting Builds

- **Mermaid errors**: Check Chrome installation and diagram syntax
- **LaTeX errors**: Review Unicode characters and math notation
- **Cross-reference warnings**: Verify label names and reference syntax
- **PDF generation**: Ensure all LaTeX packages are available

### Extension Configuration

The toolkit uses specific extension configurations that should be preserved:

- `myst_fence_as_directive = ["mermaid"]` for diagram blocks
- `numfig = True` for figure/table numbering
- Comprehensive `myst_enable_extensions` list for full functionality