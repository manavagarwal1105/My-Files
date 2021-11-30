import About from "./About"
import Home from "./Home"
import Contact from "./Contact"
import Header from "./Header"
import React from 'react';
import { BrowserRouter,Switch, Route } from "react-router-dom";

const Main = () => {
    return (
        <BrowserRouter>
        <>
        <Header/>
        <Switch>

        <Route path="/" exact component ={Home}/>
        <Route path="/About" component ={About}/>
        <Route path="/Contact" component ={Contact}/>
        

        </Switch>
        </>
        </BrowserRouter>
    )
}


export default Main