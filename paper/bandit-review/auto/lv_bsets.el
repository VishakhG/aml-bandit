(TeX-add-style-hook
 "lv_bsets"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "letterpaper")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("geometry" "margin=1in")))
   (TeX-run-style-hooks
    "latex2e"
    "../common/defs"
    "introduction"
    "background"
    "related"
    "methodology"
    "cohort_creation"
    "experiments"
    "baselines"
    "article"
    "art10"
    "proceed2e"
    "geometry"
    "times")
   (LaTeX-add-bibliographies
    "../common/refs.bib"))
 :latex)

