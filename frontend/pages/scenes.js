import { useEffect, useState } from 'react'
import Head from 'next/head'
import Navbar from '../components/Navbar'
import { apiRequest, getAuthToken, clearAuthToken } from '../lib/api'
import { useRouter } from 'next/router'

export default function ScenesPage() {
  const router = useRouter()
  const [projectId, setProjectId] = useState('')
  const [scripts, setScripts] = useState([])
  const [scenes, setScenes] = useState([])
  const [status, setStatus] = useState('')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  useEffect(() => {
    if (!getAuthToken()) {
      router.push('/login')
      return
    }
  }, [])

  const fetchScripts = async () => {
    if (!projectId) return
    setLoading(true)
    setError('')

    try {
      const data = await apiRequest(`/scripts/projects/${projectId}`)
      setScripts(data)
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  const generateScenes = async (scriptPublicId) => {
    setLoading(true)
    setError('')
    setStatus('Generating scenes…')

    try {
      const data = await apiRequest(`/scenes/${scriptPublicId}/generate-scenes`, {
        method: 'POST',
      })
      setScenes(data)
      setStatus('Scenes generated successfully')
    } catch (err) {
      setError(err.message)
      setStatus('')
    } finally {
      setLoading(false)
    }
  }

  const generateImages = async (scriptPublicId) => {
    setLoading(true)
    setError('')
    setStatus('Generating images…')

    try {
      const data = await apiRequest(`/image/scripts/${scriptPublicId}/generate-images`, {
        method: 'POST',
      })
      setScenes(data)
      setStatus('Images generated successfully')
    } catch (err) {
      setError(err.message)
      setStatus('')
    } finally {
      setLoading(false)
    }
  }

  const generateAudios = async (scriptPublicId) => {
    setLoading(true)
    setError('')
    setStatus('Generating audios…')

    try {
      const data = await apiRequest(`/audio/scripts/${scriptPublicId}/generate-audios`, {
        method: 'POST',
      })
      setScenes(data)
      setStatus('Audios generated successfully')
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
        <title>Scenes | AI Reel Studio</title>
      </Head>
      <Navbar />
      <main className="min-h-screen bg-slate-950 text-slate-100 px-6 py-10">
        <div className="mx-auto max-w-6xl space-y-8">
          <section className="rounded-3xl border border-slate-800 bg-slate-900/90 p-8 shadow-xl shadow-slate-900/40">
            <h1 className="text-3xl font-semibold text-white">Scenes</h1>
            <p className="mt-3 text-slate-400">Generate scenes, images, and audio for a script.</p>

            <div className="grid gap-4 md:grid-cols-2">
              <label className="block">
                <span className="text-sm text-slate-300">Project Public ID</span>
                <input
                  value={projectId}
                  onChange={(e) => setProjectId(e.target.value)}
                  className="mt-2 w-full rounded-3xl border border-slate-700 bg-slate-950 px-4 py-3 text-slate-100 outline-none transition focus:border-slate-500"
                />
              </label>
              <button
                type="button"
                onClick={fetchScripts}
                className="mt-6 rounded-3xl bg-slate-100 px-5 py-3 text-slate-950 transition hover:bg-white/90"
              >
                Load scripts
              </button>
            </div>

            {status && <p className="mt-4 text-slate-300">{status}</p>}
            {error && <p className="mt-4 text-rose-400">{error}</p>}
          </section>

          <section className="space-y-4">
            {scripts.map((script) => (
              <div key={script.public_id} className="rounded-3xl border border-slate-800 bg-slate-900/90 p-6 shadow-xl shadow-slate-900/20">
                <div className="flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
                  <div>
                    <h3 className="text-xl font-semibold text-white">{script.prompt}</h3>
                    <p className="mt-2 text-slate-400">Status: {script.status}</p>
                  </div>
                  <div className="flex flex-wrap gap-3">
                    <button
                      type="button"
                      onClick={() => generateScenes(script.public_id)}
                      className="rounded-full bg-sky-500 px-4 py-2 text-sm font-semibold text-white transition hover:bg-sky-400"
                    >
                      Generate scenes
                    </button>
                    <button
                      type="button"
                      onClick={() => generateImages(script.public_id)}
                      className="rounded-full bg-emerald-500 px-4 py-2 text-sm font-semibold text-white transition hover:bg-emerald-400"
                    >
                      Generate images
                    </button>
                    <button
                      type="button"
                      onClick={() => generateAudios(script.public_id)}
                      className="rounded-full bg-violet-500 px-4 py-2 text-sm font-semibold text-white transition hover:bg-violet-400"
                    >
                      Generate audios
                    </button>
                  </div>
                </div>
              </div>
            ))}
          </section>

          <section className="rounded-3xl border border-slate-800 bg-slate-900/90 p-8 shadow-xl shadow-slate-900/40">
            <h2 className="text-2xl font-semibold text-white">Scenes output</h2>
            {scenes.length === 0 ? (
              <p className="mt-4 text-slate-400">Scene data will appear here after generation.</p>
            ) : (
              <div className="mt-6 space-y-4">
                {scenes.map((scene) => (
                  <div key={scene.public_id} className="rounded-3xl border border-slate-800 bg-slate-950/80 p-5">
                    <div className="flex flex-col gap-2 md:flex-row md:items-center md:justify-between">
                      <div>
                        <h3 className="text-lg font-semibold text-white">Scene {scene.scene_number}</h3>
                        <p className="mt-2 text-slate-400">{scene.narration}</p>
                      </div>
                      <div className="text-right text-slate-300">
                        <p>Image status: {scene.image_status || 'pending'}</p>
                        <p>Audio status: {scene.audio_status || 'pending'}</p>
                      </div>
                    </div>
                    {scene.image_url && (
                      <div className="mt-4 rounded-3xl border border-slate-800 bg-slate-900 p-4 text-slate-100">
                        <p className="text-sm uppercase tracking-[0.2em] text-slate-400">Image URL</p>
                        <p className="mt-2 text-slate-300">{scene.image_url}</p>
                      </div>
                    )}
                  </div>
                ))}
              </div>
            )}
          </section>
        </div>
      </main>
    </>
  )
}
