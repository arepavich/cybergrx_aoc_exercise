# CyberGRX Take Home Assessment
CyberGRX technical assessment using Advent of Code challenge 10 (and a really nice reminder that Advent of Code exists!)

# Base requirements
Python 3.5+

# Optional dependencies
pytest (7.1.1)

# Approach
It's been quite a while since I've had reason to dig into data structures, but this seemed like a perfect use case for a stack (implemented through a list in this solution).
I took a stab at a TDD approach (something I'm still working on gaining familiarity with) to the project which I think helped keep things slimmed down quite effectively.  
  
Leveraging a dictionary (`CHUNK_METADATA`) for the purpose of associating start- and end-characters for chunks allowed for good extensibility, as well as easy lookups for scoring - if additional characters are designated in the future, it's simple to adjust the definition at the top of the main module. In hindsight, I think I would have liked to revisit the top-level structure, as the keys aren't used in a practical fashion at all. The top level structure would probably have made more sense as a tuple.

# Towards a better solution
This solution was developed strictly with the "happy path" in mind and with the specific use case described by the challenge text. Given more time with the project, I would have liked to implement error handling to gracefully handle any unexpected inputs.  
  
Additionally, I left a TODO comment in regarding a refactor I would have liked to implement in the interest of minimizing the amount of processing needed for a combination of validation and autocompletion of a given line. If scoring had not been a factor, it would have made a lot more sense to pass repairable lines through to the `repair_navdata` function during the validation process. I have a couple of ideas in mind for how that approach might still be ideal, but it seemed prudent to consider this for a future refactor instead of an immediate solution given the time constraint.
