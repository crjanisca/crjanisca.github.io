import React from "react"
import ReactDom from "react-dom"

const navbar = (
    <nav>
        <h1>Cru's Website</h1>
        <ul>
            <li>Home</li>
            <li>About</li>
            <li>Contact</li>
        </ul>
    </nav>
)

ReactDOM.render(navbar, document.getElementById("root")) 