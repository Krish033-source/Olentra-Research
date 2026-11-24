# Research: AI Orchestration Tools

**Phase 1 task:** Compare multi-vendor AI orchestration (LLM gateway) solutions and recommend the best fit for our use case.

## Summary

I researched five tools that sit between an application and multiple LLM providers (OpenAI, Claude, Gemini) and handle routing, fallbacks, load balancing and cost tracking:

| Tool | Type |
|---|---|
| LiteLLM | Open-source Python SDK + self-hosted proxy |
| Portkey | Open-source gateway + managed SaaS (observability-first) |
| OpenRouter | Managed API aggregator (one API, one balance) |
| Cloudflare AI Gateway | Managed edge gateway |
| Vercel AI Gateway | Managed gateway (best with Vercel / AI SDK) |

## Final recommendation

**LiteLLM** (self-hosted proxy) is the best fit for our use case: free to run, OpenAI-compatible, supports OpenAI + Claude + Gemini, and has built-in routing, load balancing, retries, fallbacks and budgets.
**OpenRouter** is the best option if we need something working in under an hour with zero infrastructure.

## Files in this repo

- [`comparison.md`](./comparison.md): full feature, pricing and integration comparison table
- [`recommendation.md`](./recommendation.md): decision, reasoning, rejected options, risks
- [`demo/`](./demo): small working LiteLLM demo (one code path calling OpenAI, Claude and Gemini, plus fallback and load balancing)

## Run the demo

```bash
cd demo
pip install -r requirements.txt
cp .env.example .env      # add your own API keys
python litellm_demo.py
```

## Note on accuracy

Pricing and features change often. Everything here was checked against official docs and pricing pages in **November 2026**. Please re-verify before making a purchase decision. Sources are listed at the bottom of `comparison.md`.
