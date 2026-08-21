import { useEffect, useState } from 'react'
import Head from 'next/head'
import { apiRequest, getAuthToken, clearAuthToken } from '../lib/api'
import { useRouter } from 'next/router'

export default function VideosPage() {
  const router = useRouter()
  const [scriptId, setScriptId] = useState('')
  const [status, setStatus] = useState('')
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)
  const [videoUrl, setVideoUrl] = useState('')
  const [sceneVideos, setSceneVideos] = useState([])

  useEffect(() => {
    if (!getAuthToken()) {
      router.push('/login')
      return
    }

    const sid = router.query.script_public_id || router.query.scriptId || ''
    if (sid) {
      setScriptId(sid)
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [router.query.script_public_id, router.query.scriptId])

  const handleGenerateSceneVideo = async () => {
    setError('')
    setStatus('Generating scene videos…')
    setLoading(true)

    try {
      const data = await apiRequest(`/video/scripts/${scriptId}/generate-videos`, {
        method: 'POST',
      })
      setSceneVideos(data)
      setStatus('Scene videos generated')
    } catch (err) {
      setError(err.message)
      setStatus('')
    } finally {
      setLoading(false)
    }
  }

  const handleGenerateFinalVideo = async () => {
    setError('')
    setStatus('Generating final video…')
    setLoading(true)

    try {
      const data = await apiRequest(`/video/script/${scriptId}`, {
        method: 'POST',
      })
      setVideoUrl(data.video_url)
      setStatus('Final video generated')
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
        <title>Videos | AI Reel Studio</title>
      </Head>
      <main className="min-h-screen bg-slate-950 text-slate-100 px-6 py-10">
        <div className="mx-auto max-w-6xl space-y-8">
          <section className="rounded-3xl border border-slate-800 bg-slate-900/90 p-8 shadow-xl shadow-slate-900/40">
            <h1 className="text-3xl font-semibold text-white">Videos</h1>
            <p className="mt-3 text-slate-400">Generate scene videos and a final reel.</p>

            <label className="block mt-6">
              <span className="text-sm text-slate-300">Script Public ID</span>
              <input
                value={scriptId}
                onChange={(e) => setScriptId(e.target.value)}
                className="mt-2 w-full rounded-3xl border border-slate-700 bg-slate-950 px-4 py-3 text-slate-100 outline-none transition focus:border-slate-500"
              />
            </label>

            <div className="mt-6 flex flex-col gap-4 md:flex-row">
              <button
                type="button"
                onClick={handleGenerateSceneVideo}
                disabled={!scriptId || loading}
                className="rounded-3xl bg-slate-100 px-5 py-3 text-slate-950 transition hover:bg-white/90 disabled:cursor-not-allowed disabled:opacity-60"
              >
                Generate scene videos
              </button>
              <button
                type="button"
                onClick={handleGenerateFinalVideo}
                disabled={!scriptId || loading}
                className="rounded-3xl bg-slate-100 px-5 py-3 text-slate-950 transition hover:bg-white/90 disabled:cursor-not-allowed disabled:opacity-60"
              >
                Generate final video
              </button>
            </div>

            {status && <p className="mt-4 text-slate-300">{status}</p>}
            {error && <p className="mt-4 text-rose-400">{error}</p>}
          </section>

          <section className="rounded-3xl border border-slate-800 bg-slate-900/90 p-8 shadow-xl shadow-slate-900/40">
            <h2 className="text-2xl font-semibold text-white">Results</h2>

            {sceneVideos.length === 0 ? (
              <p className="mt-4 text-slate-400">Scene video paths appear here after generation.</p>
            ) : (
              <div className="mt-6 space-y-3">
                {sceneVideos.map((item) => (
                  <div key={item.scene_number} className="rounded-3xl border border-slate-800 bg-slate-950/80 p-4 text-slate-100">
                    <p>Scene {item.scene_number}: {item.video_path}</p>
                  </div>
                ))}
              </div>
            )}

            {videoUrl && (
              <div className="mt-6 rounded-3xl border border-slate-800 bg-slate-950/80 p-6 text-slate-100">
                <p className="text-slate-300">Final video URL:</p>
                <a href={videoUrl} target="_blank" rel="noreferrer" className="text-sky-400 hover:text-sky-300">
                  {videoUrl}
                </a>
              </div>
            )}
          </section>
        </div>
      </main>
    </>
  )
}
