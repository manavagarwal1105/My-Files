//MAIN PAGE

import GroupCovidTracker from "./GroupCovidTracker"
import GroupHome from "./GroupHome"
import HeaderPage from "./HeaderPage"
import {BrowserRouter, Switch, Route} from "react-router-dom"
const MainPage=() => {
    return(
        <BrowserRouter>
        <div>
    
        <HeaderPage/>
            <Switch>
                <Route path="/" component={GroupHome} exact/>
                <Route path="/GroupCovidTracker" component={GroupCovidTracker}/>
           
                
           </Switch>
    
        </div>
       
        </BrowserRouter>

    )
}
export default MainPage
