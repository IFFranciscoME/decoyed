# synthetic-cast

A Synthetic Intelligence Framework to Generate Synthetic Conversations Between Two Synthetic Agents

## Principles 

- Functional approach.
- As much logging as *requested*.
- Modularized

## Elements

- **Converse**: A protocol to guide the interaction between 2 agents.
    - *cadence*: The dynamic logic of the conversation, e.g. step-by-step, event-based, etc.
    - *utterance*: An interaction produced by an agent. For a *conversation* protocol, this will be a written/spoken intervention.

- **Agent**: An entity that is created by the grouping of attributes and functionalities.
    - *memory*: Collect, Encode, Recollect, Decode, Compress, Decompress data from/to a memory pool.
    - *cognition*: text-generation, instruction, planning.
    - *communication*: Text-to-Speech (talk), Speech-to-Text (listen).

