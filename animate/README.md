# /animate: a Claude skill by @guipaulinooo

Turns a style reference + a rough idea into a finished animated video. Every frame is drawn in code (SVG, canvas, WebGL) and rendered to MP4 with HyperFrames.

## Install (Claude Code)
1. You need Node.js 22+ and FFmpeg.
2. Install HyperFrames (open source, by HeyGen):
   claude plugin marketplace add heygen-com/hyperframes
   claude plugin install hyperframes@hyperframes
3. Put this folder at ~/.claude/skills/animate/ (the SKILL.md file must be at ~/.claude/skills/animate/SKILL.md).
4. Restart Claude Code. Type /animate and you'll see it.

## Use it
/animate
Story/Topic: a cool explainer video on how a hummingbird hovers
15 sec, 9:16

Attach 1–3 images of a style you love (an illustration, a film frame, a Pinterest pin). Use Opus and set effort to high.

Full guide: https://claude-animate-guide.vercel.app
