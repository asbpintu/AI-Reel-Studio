import Head from 'next/head'

const API_BASE = process.env.NEXT_PUBLIC_API_BASE || 'http://localhost:8000/api/v1'

export default function Home() {
  return (
    <>
      <Head>
        <title>AI Reel Studio</title>
        <meta name="description" content="AI Reel Studio frontend" />
      </Head>
      <main className="min-h-screen bg-slate-950 text-slate-100 p-6">
        <div className="mx-auto max-w-5xl space-y-8">
          <section className="rounded-3xl border border-slate-800 bg-slate-900/80 p-8 shadow-xl shadow-slate-900/20">
            <h1 className="text-4xl font-bold text-white">AI Reel Studio</h1>
            <p className="mt-4 max-w-2xl text-slate-300">
              Create reels with AI-powered script, scene, image, audio and video generation.
            </p>
          </section>

          <section className="grid gap-4 md:grid-cols-2">
            <Card title="Projects" description="Create and manage your reel projects." href="/projects" />
            <Card title="Scripts" description="Generate scripts and manage script metadata." href="/scripts" />
            <Card title="Scenes" description="Generate scenes, images, and audio." href="/scenes" />
            <Card title="Videos" description="Create scene videos and final reels." href="/videos" />
          </section>
        </div>
      </main>
    </>
  )
}

function Card({ title, description, href }) {
  return (
    <a
      href={href}
      className="block rounded-3xl border border-slate-800 bg-slate-900/80 p-6 text-left transition hover:-translate-y-1 hover:border-slate-600"
    >
      <h2 className="text-2xl font-semibold text-white">{title}</h2>
      <p className="mt-3 text-slate-300">{description}</p>
    </a>
  )
}
