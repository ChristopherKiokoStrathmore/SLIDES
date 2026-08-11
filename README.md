# How prepared is Kenya for a disease outbreak?

The presentation deck, on its own, for hosting.

`index.html` is the whole thing: GSAP, Three.js, Motion One, Animate.css and the
county table are all inlined, so it needs no build step, no dependencies and no
network. Any static host will serve it as-is.

```
right arrow / space   next        1 / 2 / 3   jump to a slide
left arrow            back        F           fullscreen
                                  R           replay slide 3
```

Deep links work: append `#2` or `#3` to open straight onto a slide.

This branch is generated. The source, the build script and the presenter script
live on `main`, and this branch is rebuilt from
`presentation/covid-capacity-deck.html`.
