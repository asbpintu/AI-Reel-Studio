import { useEffect, useState } from 'react'
import Head from 'next/head'
import Navbar from '../components/Navbar'
import { apiRequest, getAuthToken, clearAuthToken } from '../lib/api'
import { useRouter } from 'next/router'

export default function ScriptsPage() {
  const router = useRouter()
  const [scripts, setScripts] = useState([])
  const [projectId, setProjectId] = useState('')
  const [prompt, setPrompt] = useState('')
  const [keywords, setKeywords] = useState('')
  const [duration, setDuration] = useState(30)
  const [language, setLanguage] = useState('English')
  const [reelType, setReelType] = useState('Tech')
  const [voiceType, setVoiceType] = useState('Female')
  const [style, setStyle] = useState('Modern')
  const [status, setStatus] = useState('')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  useEffect(() => {
    if (!getAuthToken()) {
      router.push('/login')
      return
    }

    fetchScripts()
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [])

  const fetchScripts = async () => {
    setLoading(true)
    setError('')

    if (!projectId) {
      setLoading(false)
      return
    }

    try {
      const data = await apiRequest(`/scripts/projects/${projectId}`)
      setScripts(data)
    } catch (err) {
      setError(err.message)
      if (err.message.toLowerCase().includes('unauthorized')) {
        clearAuthToken()
        router.push('/login')
      }
    } finally {
      setLoading(false)
    }
  }

  const handleCreate = async (event) => {
    event.preventDefault()
    setError('')
    setLoading(true)

    try {
      const script = await apiRequest(`/scripts/projects/${projectId}`, {
        method: 'POST',
        body: JSON.stringify({
          prompt,
          keywords,
          duration_seconds: Number(duration),
          language,
          reel_type: reelType,
          voice_type: voiceType,
          style,
        }),
      })

      setScripts((prev) => [script, ...prev])
      setPrompt('')
      setKeywords('')
      setStatus('Script created')
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  const handleGenerate = async (publicId) => {
    setLoading(true)
    setError('')
    setStatus('Generating script…')

    try {
      const updated = await apiRequest(`/scripts/${publicId}/generate`, {
        method: 'POST',
      })

      setScripts((prev) => prev.map((item) => (item.public_id === publicId ? updated : item)))
      setStatus('Script generated successfully')
    } catch (err) {
      setError(err.message)
      setStatus('')
    } finally {
      setLoading(false)
    }
  }

  return (
    <>
      <Head>
        <title>Scripts | AI Reel Studio</title>
      </Head>
      <Navbar />
      <main className="min-h-screen bg-slate-950 text-slate-100 px-6 py-10">
        <div className="mx-auto max-w-6xl space-y-8">
          <section className="rounded-3xl border border-slate-800 bg-slate-900/90 p-8 shadow-xl shadow-slate-900/40">
            <h1 className="text-3xl font-semibold text-white">Scripts</h1>
            <p className="mt-3 text-slate-400">Create a script for a project and generate AI content.</p>

            <form onSubmit={handleCreate} className="mt-8 grid gap-4">
              <div className="grid gap-4 md:grid-cols-2">
                <label className="block">
                  <span className="text-sm text-slate-300">Project Public ID</span>
                  <input
                    value={projectId}
                    onChange={(e) => setProjectId(e.target.value)}
                    required
                    className="mt-2 w-full rounded-3xl border border-slate-700 bg-slate-950 px-4 py-3 text-slate-100 outline-none transition focus:border-slate-500"
                  />
                </label>
                <label className="block">
                  <span className="text-sm text-slate-300">Duration</span>
                  <input
                    value={duration}
                    onChange={(e) => setDuration(e.target.value)}
                    type="number"
                    min="5"
                    className="mt-2 w-full rounded-3xl border border-slate-700 bg-slate-950 px-4 py-3 text-slate-100 outline-none transition focus:border-slate-500"
                  />
                </label>
              </div>

              <div className="grid gap-4 md:grid-cols-3">
                <label className="block">
                  <span className="text-sm text-slate-300">Language</span>
                  <input
                    value={language}
                    onChange={(e) => setLanguage(e.target.value)}
                    className="mt-2 w-full rounded-3xl border border-slate-700 bg-slate-950 px-4 py-3 text-slate-100 outline-none transition focus:border-slate-500"
                  />
                </label>
                <label className="block">
                  <span className="text-sm text-slate-300">Reel type</span>
                  <input
                    value={reelType}
                    onChange={(e) => setReelType(e.target.value)}
                    className="mt-2 w-full rounded-3xl border border-slate-700 bg-slate-950 px-4 py-3 text-slate-100 outline-none transition focus:border-slate-500"
                  />
                </label>
                <label className="block">
                  <span className="text-sm text-slate-300">Voice type</span>
                  <input
                    value={voiceType}
                    onChange={(e) => setVoiceType(e.target.value)}
                    className="mt-2 w-full rounded-3xl border border-slate-700 bg-slate-950 px-4 py-3 text-slate-100 outline-none transition focus:border-slate-500"
                  />
                </label>
              </div>

              <label className="block">
                <span className="text-sm text-slate-300">Prompt</span>
                <textarea
                  value={prompt}
                  onChange={(e) => setPrompt(e.target.value)}
                  required
                  rows="4"
                  className="mt-2 w-full rounded-3xl border border-slate-700 bg-slate-950 px-4 py-3 text-slate-100 outline-none transition focus:border-slate-500"
                />
              </label>

              <label className="block">
                <span className="text-sm text-slate-300">Keywords</span>
                <input
                  value={keywords}
                  onChange={(e) => setKeywords(e.target.value)}
                  className="mt-2 w-full rounded-3xl border border-slate-700 bg-slate-950 px-4 py-3 text-slate-100 outline-none transition focus:border-slate-500"
                />
              </label>

              {error && <p className="text-sm text-rose-400">{error}</p>}
              {status && <p className="text-sm text-slate-300">{status}</p>}

              <button
                type="submit"
                disabled={loading}
                className="rounded-3xl bg-slate-100 px-5 py-3 text-slate-950 transition hover:bg-white/90 disabled:cursor-not-allowed disabled:opacity-60"
              >
                {loading ? 'Saving…' : 'Create script'}
              </button>
            </form>
          </section>

          <section className="rounded-3xl border border-slate-800 bg-slate-900/90 p-8 shadow-xl shadow-slate-900/40">
            <div className="flex items-center justify-between gap-4">
              <h2 className="text-2xl font-semibold text-white">Script list</h2>
              <button
                type="button"
                onClick={fetchScripts}
                className="rounded-3xl border border-slate-700 bg-slate-950 px-4 py-2 text-slate-100 transition hover:bg-slate-900"
              >
                Refresh
              </button>
            </div>

            <div className="mt-6 space-y-4">
              {scripts.length === 0 && !loading ? (
                <p className="text-slate-400">No scripts found. Add a project ID and fetch scripts.</p>
              ) : (
                scripts.map((script) => (
                  <div key={script.public_id} className="rounded-3xl border border-slate-800 bg-slate-950/80 p-5">
                    <div className="flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
                      <div>
                        <h3 className="text-xl font-semibold text-white">{script.prompt}</h3>
                        <p className="mt-2 text-slate-400">Status: {script.status}</p>
                      </div>
                      <button
                        type="button"
                        onClick={() => handleGenerate(script.public_id)}
                        className="rounded-full bg-sky-500 px-4 py-2 text-sm font-semibold text-white transition hover:bg-sky-400"
                      >
                        Generate
                      </button>
                    </div>
                    {script.generated_script && (
                      <div className="mt-4 rounded-3xl border border-slate-800 bg-slate-900 p-4 text-slate-200">
                        <h4 className="text-sm font-semibold text-slate-300">Generated Script</h4>
                        <p className="mt-2 whitespace-pre-line text-slate-100">{script.generated_script}</p>
                      </div>
                    )}
                  </div>
                ))
              )}
            </div>
          </section>
        </div>
      </main>
    </>
  )
}
