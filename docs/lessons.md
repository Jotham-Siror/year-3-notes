# Lessons

## Entries
2026-10-12 · Baseplate at 45 °C inside a refinement box; white patch in the surface plot → an Icepak mesh sub-region box cut partway through the plate and that part became air → start the box at the solid's face; partb.py asserts no box cuts a solid
2026-10-12 · Refinement boxes still meshed as air solids → `obj.model = False` sets a plain Python attribute and changes nothing → `modeler.set_object_model_state([name], model=False)`, read back "Model"
2026-10-12 · Second design in one script fails "Specified version 2025.2 is not installed" → a new PyAEDT handle after `release_desktop()` in the same process fails the student version check → detach once, at the end
2026-10-12 · `duplicate_design` fails with gRPC "Paste" → AEDT copies designs through the Windows clipboard, which another program held → build each design from scratch (`build.make_enclosure`)
2026-10-12 · A design "solved" in 0 s with no geometry → opening a design name that does not exist creates an empty one → assert the name is in `design_list` before opening it
2026-10-12 · Monitor histories matched to the wrong module → `monitor.all_monitors` is not in file order and mirror-symmetric modules end at equal values → map `S<n>_MON<id>` files by the monitor ID in the saved .aedt
2026-10-12 · AEDT gone in the morning, project left with a stale `.aedt.lock` → AEDT exited overnight while the project was open → delete the lock (it names the dead process ID) before reopening
