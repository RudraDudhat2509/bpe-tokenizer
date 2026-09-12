# build-your-own-llm

An AI agent stack built entirely from scratch, stage by stage: tokenizer,
autograd engine, neural network, transformer, training loop, training
data, serving engine, vector database, and finally the agent that ties
it all together — deployed to the cloud, not just running on a laptop.

Full roadmap and reasoning: see the design spec (kept in the main
`altagic` workspace at
`docs/superpowers/specs/2026-09-12-build-your-own-llm-stack-design.md`).

Every stage lives in its own numbered folder. Each stage has a scaffold
(interface + tests) provided, and the actual implementation written by
hand.

## Stages

- [ ] `01_tokenizer` — byte-pair encoding (BPE), from scratch
- [ ] `02_autograd` — backprop engine
- [ ] `03_basic_nn` — char-level language model
- [ ] `04_attention` — scaled dot-product attention, from raw matrix ops
- [ ] `05_transformer` — full GPT architecture
- [ ] `06_training_loop` — optimizer + training loop, own weights
- [ ] `07_training_data` — data pipeline
- [ ] `08_serving` — inference engine
- [ ] `09_vector_db` — brute-force → graph search → HNSW
- [ ] `10_agent` — tie it all together
- [ ] `11_containerize` — Docker
- [ ] `12_cloud_deploy` — AWS EC2 + S3
- [ ] `13_cicd` — GitHub Actions
- [ ] `14_observability` — OpenTelemetry / Langfuse on the deployed agent
