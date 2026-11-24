# Recommendation

## Decision

**Use LiteLLM (self-hosted proxy) as our AI orchestration layer.**

## Assumed use case

> Edit this section to match the real company requirements.

- Small team / startup building an AI-powered product
- Needs OpenAI, Claude and Gemini behind one API
- Needs fallbacks so one provider outage does not break the product
- Cost-conscious: prefers no per-request gateway fees
- Comfortable running a Docker service

## Why LiteLLM

1. **Cost:** The open-source proxy is free. We only pay for hosting and model usage.
2. **Coverage:** Supports OpenAI, Claude and Gemini (and 100+ other providers) behind one OpenAI-compatible API, so existing code needs almost no change.
3. **Reliability:** Built-in retries, timeouts, fallbacks and load balancing across keys or providers.
4. **Control:** Virtual keys, per-team budgets and spend tracking. Our API keys and traffic stay in our own infrastructure.
5. **No lock-in:** Because it is open source and OpenAI-compatible, we can switch to another gateway later with minimal changes.

## Why not the others

| Tool | Reason not chosen as primary |
|---|---|
| Portkey | Excellent observability, but hosted pricing scales with logs and advanced features are paid. Good future add-on if we need deeper tracing. |
| OpenRouter | Fastest to start, but we pay a credit purchase fee and have less control. Good for prototyping. |
| Cloudflare AI Gateway | Easy and free to start, but not self-hostable and routing is less flexible. |
| Vercel AI Gateway | Only a strong fit if our stack is already on Vercel. |

## When to choose something else

- **No one wants to run infrastructure:** choose OpenRouter or hosted Portkey.
- **We need deep tracing and prompt management:** add Portkey, or pair LiteLLM with Langfuse.
- **Everything already runs on Cloudflare or Vercel:** use that platform's gateway.

## Risks and limitations

- We must host, monitor and upgrade the proxy ourselves.
- Full features (admin UI, budgets, caching) need Postgres and Redis.
- Some features (SSO, tag budgets, some guardrails) require the paid Enterprise license.
- The proxy is an extra hop, so adds a little latency (roughly tens of milliseconds in third-party benchmarks; we have not benchmarked it ourselves).
- Pricing and features of every tool change quickly, so this decision should be reviewed in a few months.

## Suggested next steps

1. Run the demo in `demo/` to confirm fallback and routing behave as expected.
2. Deploy the LiteLLM proxy with Docker and a Postgres database.
3. Create virtual keys per team or service with monthly budgets.
4. Point one existing service at the proxy by changing only `base_url`.
5. Add monitoring (Langfuse or similar) if deeper tracing is needed.
