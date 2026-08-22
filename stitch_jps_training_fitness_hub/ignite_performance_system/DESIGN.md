---
name: Ignite Performance System
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#e4bfb1'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#aa897d'
  outline-variant: '#5b4137'
  surface-tint: '#ffb599'
  primary: '#ffb599'
  on-primary: '#5a1c00'
  primary-container: '#ff5f05'
  on-primary-container: '#531900'
  inverse-primary: '#a73b00'
  secondary: '#ffb0cc'
  on-secondary: '#640038'
  secondary-container: '#ff45a1'
  on-secondary-container: '#580031'
  tertiary: '#9ecaff'
  on-tertiary: '#003258'
  tertiary-container: '#0098fc'
  on-tertiary-container: '#002e52'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdbce'
  primary-fixed-dim: '#ffb599'
  on-primary-fixed: '#370e00'
  on-primary-fixed-variant: '#7f2b00'
  secondary-fixed: '#ffd9e4'
  secondary-fixed-dim: '#ffb0cc'
  on-secondary-fixed: '#3e0021'
  on-secondary-fixed-variant: '#8d0051'
  tertiary-fixed: '#d1e4ff'
  tertiary-fixed-dim: '#9ecaff'
  on-tertiary-fixed: '#001d36'
  on-tertiary-fixed-variant: '#00497d'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
  electric-orange: '#FF8A00'
  vibrant-pink: '#E01E5A'
  steel-silver: '#C0C0C0'
  brushed-metal: '#2A2A2A'
  surface-elevated: '#1E1E1E'
typography:
  display-xl:
    fontFamily: Montserrat
    fontSize: 72px
    fontWeight: '900'
    lineHeight: 72px
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: Montserrat
    fontSize: 48px
    fontWeight: '800'
    lineHeight: 52px
    letterSpacing: -0.02em
  headline-lg-mobile:
    fontFamily: Montserrat
    fontSize: 32px
    fontWeight: '800'
    lineHeight: 36px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Montserrat
    fontSize: 24px
    fontWeight: '700'
    lineHeight: 32px
  body-lg:
    fontFamily: Hanken Grotesk
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Hanken Grotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.1em
  stat-value:
    fontFamily: Montserrat
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 32px
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 8px
  margin-mobile: 20px
  margin-desktop: 64px
  gutter: 24px
  section-gap: 80px
---

## Brand & Style

The brand personality is high-octane, elite, and relentlessly professional. It is designed for serious athletes and fitness enthusiasts who demand intensity and precision. The visual language bridges the gap between raw physical effort and sophisticated performance tracking.

The design style is **High-Contrast / Modern with Tactile influences**. It utilizes a deep dark-mode foundation to make high-energy gradients and metallic textures pop. The aesthetic is inspired by premium automotive interfaces and high-end gym equipment, using subtle glows and "machined" details to evoke a sense of power and durability.

Key visual pillars:
- **Kinetic Energy:** Use of diagonal lines and aggressive gradients.
- **Machined Precision:** Metallic accents and sharp, intentional spacing.
- **High-Impact Imagery:** Gritty, high-contrast photography with dramatic lighting (Chiaroscuro).

## Colors

The palette is centered on a "Core Heat" gradient that transitions from a fiery Electric Orange to a Deep Pink. This gradient represents the intensity of training and the spectrum of energy.

- **Primary:** Electric Orange (#FF5F05) is used for primary calls to action and critical performance metrics.
- **Secondary:** Deep Pink (#EC008C) provides a sophisticated counterpoint, used for secondary interactions and accent details.
- **Neutral:** A rich, obsidian black (#121212) serves as the base, providing maximum contrast for the accent colors.
- **Surface Strategy:** Use `surface-elevated` (#1E1E1E) for card containers to create subtle separation without breaking the dark-mode immersion.
- **Metallic Accents:** Steel Silver is reserved for iconography and borders that mimic brushed aluminum or chrome gym hardware.

## Typography

The typography system is built for impact and legibility under pressure.

- **Headlines:** Montserrat in Heavy/ExtraBold weights is used to convey strength. For large display text, use tight letter spacing to create a compact, "heavy" visual footprint.
- **Body:** Hanken Grotesk provides a modern, high-tech feel that is exceptionally readable on dark backgrounds.
- **Metrics/Labels:** JetBrains Mono is introduced for technical data, rep counts, and timestamps, reinforcing the "performance tracking" aspect of the brand.
- **Styling:** Headings should frequently utilize uppercase transformations to maximize the athletic aesthetic.

## Layout & Spacing

The layout follows a **Fluid Grid** model with high-density information areas balanced by significant vertical breathing room between major sections.

- **Grid:** A 12-column system for desktop and a 4-column system for mobile.
- **Rhythm:** An 8px base unit drives all padding and margins. 
- **Asymmetry:** To emphasize "energy," use diagonal clipping paths on section headers or background elements to create a sense of forward motion.
- **Mobile Reflow:** For mobile views, move high-intensity actions (like "Start Workout") to a fixed bottom-bar position with a "heat-map" gradient background.

## Elevation & Depth

This system ignores traditional soft shadows in favor of **Tonal Layers and Glows**.

- **Layers:** Depth is communicated by increasing the lightness of the background color. Surface levels: Base (#121212) -> Level 1 (#1E1E1E) -> Level 2 (#2A2A2A).
- **Glows:** Interactive elements like active buttons use an outer "aura" glow rather than a shadow. This glow uses the primary orange color at 30% opacity with a large blur radius (20px+).
- **Metallic Surfaces:** Apply a subtle 1px "top light" highlight to cards and buttons—a thin, high-contrast line at the top edge to simulate overhead gym lighting hitting a metallic edge.
- **Backdrop Blur:** Use heavy backdrop blurs (20px) on navigation bars and overlays to maintain focus on the content while hinting at the vibrant background gradients.

## Shapes

The shape language is **aggressive and technical**. 

- **Primary Corners:** Use a "Soft" (4px - 8px) radius for most UI elements. This prevents the UI from feeling too "friendly" (rounded) or too "retro" (sharp).
- **Angled Elements:** Incorporate 15-degree diagonal cuts on button edges or decorative containers to reinforce the "athletic" narrative.
- **Containers:** Cards should use a subtle 1px border in `brushed-metal` to define their boundaries against the dark background.

## Components

### Buttons
Primary buttons use the orange-to-pink gradient with white uppercase text. They feature a "metallic sheen" overlay (a linear gradient at 45 degrees with white at 10% opacity) and an outer glow on hover.

### Progress Bars & Rings
These are central to the experience. Use high-contrast gradients for the "filled" portion, with a `brushed-metal` background for the "empty" track. Add a glow effect to the leading edge of the progress bar to signify "current energy."

### Cards (Workouts/Stats)
Cards use `surface-elevated` with no shadow, defined instead by a 1px `brushed-metal` border. High-impact cards may feature a partial background image with a dark overlay and vibrant typography.

### Input Fields
Inputs are minimalist: a bottom border only in `steel-silver`. When focused, the border transitions to the primary gradient and a subtle glow appears beneath the text.

### Chips & Badges
Small, high-contrast tags used for difficulty levels (e.g., "Advanced") or muscle groups. These should use solid `vibrant-pink` backgrounds with black text for maximum punch.

### Performance Charts
Line charts should use a thick, primary-gradient stroke with a semi-transparent gradient fill underneath (fading to 0% opacity at the baseline).