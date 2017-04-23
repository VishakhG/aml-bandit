(TeX-add-style-hook
 "baselines"
 (lambda ()
   (LaTeX-add-labels
    "my-label"
    "fig:aspirin-test"
    "fig:aspirin-train"
    "fig:aspirin_precision"
    "fig:cancer-test"
    "fig:cancer-train"
    "fig:cancer_precision"))
 :latex)

