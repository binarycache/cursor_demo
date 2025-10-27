# Ethereum Converter - Design System

## 🎨 Color Palette

### Primary Gradient
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```
- **Primary Start**: `#667eea` (Purple-Blue)
- **Primary End**: `#764ba2` (Deep Purple)

### Neutral Colors
| Color | Value | Usage |
|-------|-------|-------|
| White | `#ffffff` | Container background, card text |
| Dark Gray | `#333333` | Headings |
| Medium Gray | `#666666` | Subtitles, secondary text |
| Light Gray | `#e0e0e0` | Input borders, button borders |
| Lighter Gray | `#f5f5f5` | Button background (hover), info box |
| Darker Gray | `#f8f9fa` | Info box background |

### Interactive Colors
```css
/* Primary Action */
.btn-convert: #667eea to #764ba2 (gradient)
.btn-convert-hover: rgba(102, 126, 234, 0.4) (shadow)

/* Secondary Action */
.btn-clear: #f5f5f5 → #e0e0e0 (on hover)

/* Success Action */
.btn-copy: #4caf50 → #45a049 (on hover)

/* Focus State */
border-color: #667eea
box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1)
```

## 🔤 Typography

### Font Family
```css
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
```
**Primary**: System font stack (San Francisco on macOS, Segoe UI on Windows)

**Monospace**: `'Courier New', monospace` (for displaying numeric values)

### Type Scale
| Element | Font Size | Weight | Line Height | Usage |
|---------|-----------|--------|-------------|-------|
| H1 | `2rem` (32px) | 600 | Auto | Page title |
| H3 | `1rem` (16px) | 600 | Auto | Section headings |
| Body | `1rem` (16px) | 400 | Auto | Default text |
| Small | `0.95rem` (15.2px) | 400 | Auto | Subtitles |
| XSmall | `0.85rem` (13.6px) | 400 | Auto | Result labels |
| Large | `1.5rem` (24px) | 600 | Auto | Result values |
| Button | `1rem` (16px) | 600 | Auto | Button text |

### Text Colors
```css
/* Headings */
color: #333;

/* Body Text */
color: #666;

/* White Text */
color: white; /* On colored backgrounds */
```

## 📐 Spacing System

### Padding/Margins
| Size | Value | Usage |
|------|-------|-------|
| XS | `5px` | Tight spacing (between label and value) |
| S | `10px` | Gap between elements (input-group, buttons) |
| M | `15px` | Standard padding (inputs, info-box text) |
| L | `20px` | Section margins, button groups |
| XL | `30px` | Section spacing |
| XXL | `40px` | Container padding |
| Page | `20px` | Body padding |

### Border Radius
| Element | Value | Usage |
|---------|-------|-------|
| Container | `20px` | Main card |
| Cards/Buttons | `10px` | Inputs, buttons, info box |
| Result Cards | `12px` | Result display cards |

## 🎯 Shadows

```css
/* Container Shadow */
box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);

/* Hover Shadow */
box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);

/* Toast Shadow */
box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
```

## 📱 Responsive Breakpoints

```css
@media (max-width: 600px) {
    /* Mobile adjustments */
    .container {
        padding: 20px;
    }
    
    .input-group {
        flex-direction: column;
    }
    
    h1 {
        font-size: 1.5rem;
    }
}
```

## 🎭 Animation/Transitions

### Durations
- **Standard**: `0.3s` (all interactive elements)
- **Toast**: `0.3s` (slide in/out)

### Easings
- **Ease**: `cubic-bezier(0.25, 0.1, 0.25, 1)`

### Interactions
```css
/* Hover Elevation */
transform: translateY(-2px);

/* Focus Glow */
box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
```

## 🎨 Design Tokens Summary

```css
:root {
  /* Colors */
  --color-primary-start: #667eea;
  --color-primary-end: #764ba2;
  --color-primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  
  --color-white: #ffffff;
  --color-dark: #333333;
  --color-medium: #666666;
  --color-light: #e0e0e0;
  --color-lighter: #f5f5f5;
  --color-info-bg: #f8f9fa;
  
  --color-success: #4caf50;
  --color-success-hover: #45a049;
  
  --color-focus: #667eea;
  --color-focus-glow: rgba(102, 126, 234, 0.1);
  
  /* Typography */
  --font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
  --font-mono: 'Courier New', monospace;
  
  --font-size-h1: 2rem;
  --font-size-h3: 1rem;
  --font-size-body: 1rem;
  --font-size-subtitle: 0.95rem;
  --font-size-label: 0.85rem;
  --font-size-result: 1.5rem;
  
  --font-weight-bold: 600;
  --font-weight-normal: 400;
  
  /* Spacing */
  --spacing-xs: 5px;
  --spacing-s: 10px;
  --spacing-m: 15px;
  --spacing-l: 20px;
  --spacing-xl: 30px;
  --spacing-xxl: 40px;
  
  /* Border Radius */
  --radius-sm: 10px;
  --radius-md: 12px;
  --radius-lg: 20px;
  
  /* Shadows */
  --shadow-container: 0 20px 60px rgba(0, 0, 0, 0.3);
  --shadow-hover: 0 5px 15px rgba(102, 126, 234, 0.4);
  --shadow-toast: 0 5px 15px rgba(0, 0, 0, 0.2);
  
  /* Transitions */
  --transition-fast: 0.3s ease;
  
  /* Layout */
  --container-max-width: 600px;
  --container-padding: 40px;
}
```

## 📊 Component Specifications

### Container
- **Max Width**: `600px`
- **Padding**: `40px` (desktop), `20px` (mobile)
- **Background**: `white`
- **Border Radius**: `20px`
- **Shadow**: `0 20px 60px rgba(0, 0, 0, 0.3)`

### Inputs
- **Padding**: `15px`
- **Border**: `2px solid #e0e0e0`
- **Border Radius**: `10px`
- **Font Size**: `1rem`
- **Focus**: Border changes to `#667eea` with glow effect

### Buttons
- **Padding**: `15px`
- **Border Radius**: `10px`
- **Font Size**: `1rem`
- **Font Weight**: `600`
- **Hover**: Elevate by `-2px` with shadow

### Result Cards
- **Background**: Primary gradient
- **Padding**: `20px`
- **Border Radius**: `12px`
- **Color**: `white`
- **Font Family**: Monospace for values

### Information Box
- **Background**: `#f8f9fa`
- **Padding**: `15px`
- **Border Radius**: `10px`
- **Font Size**: `0.9rem`

---

**Design Philosophy**: Clean, modern, gradient-based UI with excellent accessibility and responsive design. Uses system fonts for native feel and monospace fonts for precise numerical display.

