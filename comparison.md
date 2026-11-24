# Comparison of AI Orchestration Tools

*Checked: November 2026. Verify on official pages before buying anything.*

## 1. Overview

| | LiteLLM | Portkey | OpenRouter | Cloudflare AI Gateway | Vercel AI Gateway |
|---|---|---|---|---|---|
| **What it is** | Python SDK + self-hosted proxy | AI gateway (open-source core) + hosted platform | Managed API aggregator | Managed edge gateway | Managed gateway |
| **Open source** | Yes (MIT proxy; some enterprise features under a paid license) | Yes (MIT gateway) | No | No | No |
| **Self-host** | Yes (Docker / Kubernetes) | Yes (`npx @portkey-ai/gateway`) | No | No | No |
| **Best for** | Teams who want control and low cost | Teams who want strong observability | Fastest start, many models | Teams already on Cloudflare | Teams already on Vercel / AI SDK |

## 2. Pricing

| Tool | Gateway cost | Notes |
|---|---|---|
| **LiteLLM** | Free (open source). You pay only for your own hosting. | Enterprise edition is "contact sales" (SSO, advanced controls, some budget features). |
| **Portkey** | Open source: free, self-hosted. Hosted: Dev free (10K requests/month), Production $49/month (100K requests), Enterprise custom. | Hosted pricing is based on recorded logs/requests. Semantic cache is Enterprise only. |
| **OpenRouter** | No markup on model price, but a fee when buying credits (about 5.5% by card). | Bring-your-own-key (BYOK) has a free allowance, then a 5% fee above it. Fee structure is changing, so check the pricing page. |
| **Cloudflare AI Gateway** | Available on all plans; free to start. | Log storage limits and pricing apply. Newer accounts follow Workers Logs pricing. |
| **Vercel AI Gateway** | Provider list price, zero markup (including BYOK). | Free tier includes a small monthly credit. |

## 3. Technical features

| Feature | LiteLLM | Portkey | OpenRouter | Cloudflare AI Gateway | Vercel AI Gateway |
|---|---|---|---|---|---|
| **OpenAI-compatible API** | Yes | Yes | Yes | Yes | Yes |
| **OpenAI support** | Yes | Yes | Yes | Yes | Yes |
| **Claude (Anthropic) support** | Yes | Yes | Yes | Yes | Yes |
| **Gemini support** | Yes | Yes | Yes | Yes | Yes |
| **Number of providers** | 100+ | 45+ providers (1600+ models claimed) | Large model catalog | Major providers | Major providers |
| **Model routing** | Tag-based, cost-based, latency-based, custom | Conditional routing, config-based | Provider routing + price/uptime-based | Dynamic routing (visual or JSON) | Automatic provider selection |
| **Load balancing** | Yes (least-busy, shuffle, weighted) | Yes (weighted across keys/providers) | Yes (across providers) | Limited (no documented weighted LB) | Yes (across providers) |
| **Fallbacks** | Yes (model groups, context-window fallbacks) | Yes (configurable on error codes) | Yes (automatic provider fallbacks) | Yes (fallback array, up to 5 retries) | Yes (same-model provider failover) |
| **Retries and timeouts** | Yes | Yes | Automatic | Yes | Automatic |
| **Budgets and spend limits** | Yes (per key, user, team) | Yes (paid plans) | Credit-based limits | Spend limits | Credit-based |
| **Caching** | Yes (Redis, semantic) | Simple on all plans, semantic on Enterprise | Prompt caching passthrough | Yes | Limited |
| **Observability** | Basic logging, integrates with Langfuse etc. | Strong (logs, traces, metrics) | Activity dashboard | Analytics and logs | Dashboard |
| **Guardrails** | Yes (some need Enterprise) | Yes (paid) | Limited | DLP scanning | Limited |

## 4. Ease of integration

| Tool | Integration effort | How |
|---|---|---|
| **LiteLLM** | Medium | `pip install litellm` for SDK use, or run the proxy and change only `base_url` in existing OpenAI code. Proxy needs Postgres/Redis for full features. |
| **Portkey** | Easy | Change base URL or use their SDK. Hosted version needs no infra. |
| **OpenRouter** | Very easy | Create account, add credits, change base URL and API key. |
| **Cloudflare AI Gateway** | Easy | Change base URL to the gateway URL. Needs a Cloudflare account. |
| **Vercel AI Gateway** | Very easy on Vercel | Native with AI SDK. Works elsewhere through compatible endpoints. |

## 5. Pros and cons

| Tool | Pros | Cons |
|---|---|---|
| **LiteLLM** | Free, full control, widest provider coverage, strong routing and fallbacks, data stays in our infra | We must host and maintain it; adds some latency; some enterprise features are paid |
| **Portkey** | Great observability, guardrails, easy hosted option, open-source core | Paid plans scale with log volume; advanced features are Enterprise |
| **OpenRouter** | Fastest setup, one balance for all models, large catalog | Credit purchase fee; less control; requests pass through a third party |
| **Cloudflare AI Gateway** | Easy, edge network, free to start | Not self-hostable; log limits; routing less flexible than LiteLLM |
| **Vercel AI Gateway** | Zero markup, simple | Best only if the stack is on Vercel |

## Sources (official pages)

- LiteLLM: https://docs.litellm.ai and https://github.com/BerriAI/litellm
- Portkey pricing: https://portkey.ai/pricing
- Portkey feature comparison: https://docs.portkey.ai/docs/product/product-feature-comparison
- Portkey gateway repo: https://github.com/Portkey-AI/gateway
- OpenRouter FAQ (fees): https://openrouter.ai/docs/faq
- OpenRouter pricing: https://openrouter.ai/pricing
- Cloudflare AI Gateway: https://developers.cloudflare.com/ai-gateway
- Cloudflare AI Gateway pricing: https://developers.cloudflare.com/ai-gateway/reference/pricing/
- Vercel AI Gateway: https://vercel.com/docs/ai-gateway

Third-party reviews (LiteLLM, Portkey, OpenRouter comparisons by TrueFoundry, Geekflare, Atlan) were used only to cross-check details.
