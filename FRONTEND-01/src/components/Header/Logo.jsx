import { BRAND } from "../../constants/branding"
import { Link } from "react-router-dom"



const Logo = () => {
  return (
      <div className="flex items-center space-x-3">
      <div>
        
        <Link to='/'><h1 className="text-2xl font-bold text-white">{BRAND.name}</h1></Link>
        {/* <p className="text-xs font-bold text-white">{ BRAND.tagline }</p> */}
        
          </div>
    </div>
  )
}

export default Logo