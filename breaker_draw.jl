# Breaker sortition draw — plumbline seed-file review (round 2)
# Method: Julia RandomDevice (OS entropy, /dev/urandom) — "true rand()",
# not a seeded PRNG. Single uniform draw over the candidate list.
# 2026-10-08, Tangent side chat, at Kelly's direction.

using Random

candidates = [
    "Superninja on DeepSeek",
    "Sonnet (fresh instance)",
    "Opus (fresh instance)",
    "Fable",
    "claude.ai (fresh session)",
    "Claude Code (fresh session)",
    "ChatGPT (fresh session)",
    "Gemini (fresh session)",
    "Grok (fresh session)",
    "Midjourney (image-mode; verdict would be images, translation lossy)",
]

rng = RandomDevice()  # OS entropy — true RNG, unreproducible by design
idx = rand(rng, 1:length(candidates))

println("candidates: ", length(candidates))
for (i, c) in enumerate(candidates)
    println(i, ": ", c)
end
println()
println("drawn index: ", idx)
println("breaker: ", candidates[idx])
