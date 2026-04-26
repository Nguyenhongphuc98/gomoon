---
colors:
  surface: '#f8f9ff'
  surface-dim: '#cbdbf5'
  surface-bright: '#f8f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eff4ff'
  surface-container: '#e5eeff'
  surface-container-high: '#dce9ff'
  surface-container-highest: '#d3e4fe'
  on-surface: '#0b1c30'
  on-surface-variant: '#454654'
  inverse-surface: '#213145'
  inverse-on-surface: '#eaf1ff'
  outline: '#757686'
  outline-variant: '#c5c5d7'
  surface-tint: '#3b4fd2'
  primary: '#2036bd'
  on-primary: '#ffffff'
  primary-container: '#3e52d5'
  on-primary-container: '#d7daff'
  inverse-primary: '#bbc3ff'
  secondary: '#006c49'
  on-secondary: '#ffffff'
  secondary-container: '#6cf8bb'
  on-secondary-container: '#00714d'
  tertiary: '#7e3100'
  on-tertiary: '#ffffff'
  tertiary-container: '#a44200'
  on-tertiary-container: '#ffd3bf'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dfe0ff'
  primary-fixed-dim: '#bbc3ff'
  on-primary-fixed: '#000d60'
  on-primary-fixed-variant: '#1d34ba'
  secondary-fixed: '#6ffbbe'
  secondary-fixed-dim: '#4edea3'
  on-secondary-fixed: '#002113'
  on-secondary-fixed-variant: '#005236'
  tertiary-fixed: '#ffdbcc'
  tertiary-fixed-dim: '#ffb694'
  on-tertiary-fixed: '#351000'
  on-tertiary-fixed-variant: '#7a2f00'
  background: '#f8f9ff'
  on-background: '#0b1c30'
  surface-variant: '#d3e4fe'
typography:
  h1:
    fontFamily: Manrope
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.02em
  h2:
    fontFamily: Manrope
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-sm:
    fontFamily: Manrope
    fontSize: 13px
    fontWeight: '600'
    lineHeight: 18px
    letterSpacing: 0.02em
  lunar-date:
    fontFamily: Manrope
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  container-padding: 16px
  gutter: 12px
---

## Brand & Style

The design system is rooted in **Minimalist Modernism** with a focus on functional clarity and cognitive ease. It prioritizes high legibility and intentional whitespace to reduce the stress often associated with task management. 

The aesthetic is characterized by:
- **Clarity of Purpose:** Every element serves a functional role in task completion.
- **Cultural Resonance:** Subtle integration of Vietnamese time-keeping traditions, treating the Lunar calendar with equal visual importance to the Solar calendar.
- **Modern Reliability:** Using soft elevations and refined geometry to evoke a sense of professional stability.

## Colors

The palette is designed for high accessibility and emotional balance.

- **Primary (Deep Indigo):** Used for primary actions, active states, and brand presence. It suggests reliability.
- **Success (Emerald Green):** Reserved exclusively for completed tasks and positive feedback loops.
- **Neutrals (Slate Grays):** A cool-toned gray scale provides structural hierarchy without competing with task content.
- **Lunar Accent:** A softer periwinkle shade is used specifically for Lunar calendar indicators to distinguish them from standard Solar dates.

**Dark Mode:** Transitions from a Slate-based light theme to a Deep Navy Dark theme, maintaining contrast ratios of at least 4.5:1 for all text elements.

## Typography

This design system utilizes **Manrope** for its modern, geometric qualities and excellent legibility in both English and Vietnamese (supporting all diacritics natively).

- **Hierarchy:** Strong contrast between bold headings and regular body text ensures users can scan task lists quickly.
- **Specialized Styles:** A specific italicized weight is used for Lunar dates to provide a secondary visual layer when displayed alongside Solar dates.
- **Readability:** Generous line-heights are maintained to accommodate complex Vietnamese tone marks without overlapping.

## Layout & Spacing

The system follows a **4px baseline grid** with a fluid mobile layout.

- **Margins:** 16px horizontal margins for standard mobile screens.
- **Safe Areas:** Generous vertical padding (24px+) between task categories to prevent visual clutter.
- **Touch Targets:** All interactive elements maintain a minimum hit area of 44x44px.
- **Grouping:** Use the `md` (16px) unit for spacing between related tasks and the `lg` (24px) unit for spacing between distinct sections or categories.

## Elevation & Depth

Hierarchy is established through **Ambient Shadows** and tonal layering rather than heavy borders.

- **Surface Level (0dp):** The main background.
- **Card Level (1dp):** Individual tasks or category containers. Uses a very soft, diffused shadow: `y: 4, blur: 12, color: rgba(0,0,0,0.05)`.
- **Active Level (2dp):** Modals or floating action buttons (FAB). Enhanced shadow: `y: 8, blur: 20, color: rgba(0,0,0,0.1)`.
- **Dark Mode Elevation:** Depth is communicated via lighter surface fills (e.g., Slate 800 on Slate 900) rather than shadows.

## Shapes

The shape language is friendly and approachable, utilizing **Rounded** corners to soften the UI.

- **Small Components (8px):** Checkboxes, tags, and small input fields.
- **Medium Components (12px):** Task cards, category containers, and action buttons.
- **Large Components (24px+):** Bottom sheets and modal containers (top corners only).
- **Icons:** Use a 2px stroke weight with rounded caps and joins to match the component geometry.

## Components

- **Task Cards:** White (or dark navy) surfaces with a subtle 1px border (`#E2E8F0` or `#334155`). Includes a title, time, and a distinct Lunar date indicator if applicable.
- **Lunar Toggle:** A specialized component allowing users to switch or view both Solar (Sun icon) and Lunar (Crescent Moon icon) dates within the calendar picker.
- **Primary Button:** Solid Indigo fill with 12px rounded corners and white centered text.
- **Completion Checkbox:** A circular ring that transforms into a solid Green fill with a checkmark upon interaction.
- **Category Chips:** Minimalist line-art icon paired with a text label, using a light gray background that switches to a primary tint when selected.
- **Progress Indicator:** A thin, horizontal bar at the top of category groups to show the ratio of completed vs. pending tasks.
- **Input Fields:** Bottom-aligned labels with high contrast text and 8px rounded corners, utilizing a soft gray fill to define the hit area.