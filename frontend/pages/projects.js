import { useEffect, useState } from 'react'
import Head from 'next/head'
import { apiRequest, clearAuthToken, getAuthToken } from '../lib/api'
import { useRouter } from 'next/router'

export default function ProjectsPage() {
  const router = useRouter()
  const [projects, setProjects] = useState([])
  const [name, setName] = useState('')
  const [description, setDescription] = useState('')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  useEffect(() => {
    if (!getAuthToken()) {
      router.push('/login')
      return
    }

    fetchProjects()
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [])

  const fetchProjects = async () => {
    setLoading(true)
    setError('')

    try {
      const list = await apiRequest('/projects')
      setProjects(list)
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
      const project = await apiRequest('/projects', {
        method: 'POST',
        body: JSON.stringify({ project_name: name, description }),
      })

      setProjects((prev) => [project, ...prev])
      setName('')
      setDescription('')
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  return (
    <>
      <Head>
        <title>Projects | AI Reel Studio</title>
      </Head>
      <main className="min-h-screen bg-slate-950 text-slate-100 px-6 py-10">
        <div className="mx-auto max-w-6xl space-y-8">
          <section className="rounded-3xl border border-slate-800 bg-slate-900/90 p-8 shadow-xl shadow-slate-900/40">
            <div className="flex flex-col gap-2 md:flex-row md:items-center md:justify-between">
              <div>
                <h1 className="text-3xl font-semibold text-white">Projects</h1>
                <p className="mt-2 text-slate-400">Create and manage your reel projects.</p>
              </div>
            </div>

            <form onSubmit={handleCreate} className="mt-8 space-y-4">
              <div className="grid gap-4 md:grid-cols-2">
                <label className="block">
                  <span className="text-sm text-slate-300">Project name</span>
                  <input
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    required
                    className="mt-2 w-full rounded-3xl border border-slate-700 bg-slate-950 px-4 py-3 text-slate-100 outline-none transition focus:border-slate-500"
                  />
                </label>
                <label className="block">
                  <span className="text-sm text-slate-300">Description</span>
                  <input
                    value={description}
                    onChange={(e) => setDescription(e.target.value)}
                    className="mt-2 w-full rounded-3xl border border-slate-700 bg-slate-950 px-4 py-3 text-slate-100 outline-none transition focus:border-slate-500"
                  />
                </label>
              </div>

              {error && <p className="text-sm text-rose-400">{error}</p>}

              <button
                type="submit"
                disabled={loading}
                className="rounded-3xl bg-slate-100 px-5 py-3 text-slate-950 transition hover:bg-white/90 disabled:cursor-not-allowed disabled:opacity-60"
              >
                {loading ? 'Creating…' : 'Create project'}
              </button>
            </form>
          </section>

          <section className="rounded-3xl border border-slate-800 bg-slate-900/90 p-8 shadow-xl shadow-slate-900/40">
            <h2 className="text-2xl font-semibold text-white">Your projects</h2>
            {loading && <p className="mt-4 text-slate-400">Loading projects…</p>}
            {!loading && projects.length === 0 && <p className="mt-4 text-slate-400">No projects yet. Create one above.</p>}

            <div className="mt-6 grid gap-4">
              {projects.map((project) => (
                <div
                  key={project.public_id}
                  role="button"
                  onClick={() => router.push(`/scripts?project_public_id=${project.public_id}`)}
                  className="cursor-pointer rounded-3xl border border-slate-800 bg-slate-950/80 p-5"
                >
                  <div className="flex items-center justify-between gap-4">
                    <div>
                      <h3 className="text-xl font-semibold text-white">{project.project_name}</h3>
                      <p className="mt-2 text-slate-400">{project.description || 'No description'}</p>
                    </div>
                    <span className="rounded-full bg-slate-800 px-3 py-1 text-xs uppercase tracking-[0.2em] text-slate-300">
                      {project.public_id.slice(0, 8)}
                    </span>
                  </div>
                </div>
              ))}
            </div>
          </section>
        </div>
      </main>
    </>
  )
}
