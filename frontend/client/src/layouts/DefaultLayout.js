
import Header from "../components/Header"
import '../assets/css/styles.css';
export default function DefaultLayout({children}) {
    return (
        <div>
           
            <div>
            <Header/>
        <header className="masthead">
            <div className="container">
                <div className="masthead-subheading">Welcome To Our Studio!</div>
                <div className="masthead-heading text-uppercase">It's Nice To Meet You</div>
                <a className="btn btn-primary btn-xl text-uppercase" href="#services">Tell Me More</a>
            </div>
        </header>
            {children}
            </div>
        </div>
    )
}
