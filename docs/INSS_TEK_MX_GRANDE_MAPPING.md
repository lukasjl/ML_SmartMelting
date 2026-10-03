# InssTek MX-Grande to SmartWeld/ML mapping

This is a data contract, not a claim that every DED variable is directly
supported by SmartWeld.

| MX-Grande / DED variable | ML role | SmartWeld status |
|---|---|---|
| laser power | primary input | candidate direct input |
| scan/travel speed | primary input | candidate direct input |
| laser spot diameter | primary input | candidate direct input |
| material/alloy | material input | must match material model |
| powder feed rate | DED input | not established as direct input |
| layer height | DED input | not established |
| track/layer geometry | target/measurement | requires validation |
| shielding gas | process condition | model-dependent |
| nozzle/standoff | DED geometry | not established |
| substrate/preheat temperature | thermal condition | model-dependent |
| melt-pool width | physics feature/target | candidate output |
| penetration/depth | physics feature/target | candidate output |
| thermal efficiency | physics feature | candidate output |

The ML dataset must retain all original machine inputs even when SmartWeld does
not consume them. This permits later replacement or augmentation of the
physics model without losing DED information.
