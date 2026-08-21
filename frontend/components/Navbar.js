import Link from 'next/link'
import { useRouter } from 'next/router'
import { clearAuthToken, getAuthToken } from '../lib/api'
import { useEffect, useState } from 'react'

export default function Navbar() {
  const router = useRouter()
  const [authenticated, setAuthenticated] = useState(false)

  useEffect(() => {
    setAuthenticated(Boolean(getAuthToken()))
  }, [])

  const handleLogout = () => {
    clearAuthToken()
    router.push('/login')
  }

  return (
    <header className="border-b border-slate-800 bg-slate-950/95 text-slate-100">
      <div className="mx-auto flex max-w-6xl items-center justify-between px-6 py-4">
        <Link href="/" className="text-xl font-semibold text-white">
          AI Reel Studio
        </Link>

        <nav className="flex items-center gap-4 text-sm text-slate-300">
          <Link href="/projects" className="hover:text-white">
            Projects
          </Link>
          <Link href="/scripts" className="hover:text-white">
            Scripts
          </Link>
          <Link href="/scenes" className="hover:text-white">
            Scenes
          </Link>
          <Link href="/videos" className="hover:text-white">
            Videos
          </Link>
          {authenticated ? (
            <button
              type="button"
              onClick={handleLogout}
              className="rounded-full border border-slate-700 bg-slate-900 px-4 py-2 text-slate-200 transition hover:bg-slate-800"
            >
              Logout
            </button>
          ) : (
            <Link
              href="/login"
              className="rounded-full border border-slate-700 bg-slate-900 px-4 py-2 text-slate-200 transition hover:bg-slate-800"
            >
              Login
            </Link>
          )}
        </nav>
      </div>
    </header>
  )
}
