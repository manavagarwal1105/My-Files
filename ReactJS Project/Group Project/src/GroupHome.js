//UPDATED HOME PAGEE (GroupHome.js)

import React from "react";
import './App.css';
import {FaExclamationTriangle} from "react-icons/fa";
import {RiSurgicalMaskLine} from "react-icons/ri";
import {MdCoronavirus} from "react-icons/md";
import { IconContext } from "react-icons/lib";
import prev from './prev.jpg'
import covidpeople from "./covidpeople.png"
import sym from "./sym.jpg"
const GroupHome = () => {
    return(
        <div>
            <div>


<p className= 'covid'> </p>
</div>

<h3 style={{ color: "Red", fontFamily: "Monsterrat", fontWeight: 200,textAlign: 'center',fontSize: 40  }}> <MdCoronavirus/>  Coronavirus Disease </h3>
  

      
<p style={{ color: "rgba(201, 34, 68, 0.89)", fontFamily: "Kalam", fontWeight: 300,textAlign: 'left',fontSize: 22  }} className='contentBox'>
Coronavirus disease (COVID-19) is an infectious disease caused by the SARS-CoV-2 virus. On 11 March 
2020, WHO declared Novel Coronavirus Disease (COVID-19) outbreak as a pandemic and reiterated the call 
for countries to take immediate actions and scale up response to treat, detect and reduce transmission 
to save people’s lives.
</p>

<div>

           
        </div>
<p style={{ color: "rgba(201, 34, 68, 0.89)", fontFamily: "Kalam", fontWeight: 300,textAlign: 'left',fontSize: 22  }} className='contentBox'> 
Most people infected with the virus  experience mild to moderate respiratory illness and recover without 
requiring special treatment. However, some will become seriously ill and require medical attention. Older 
people and those with underlying medical conditions like cardiovascular disease, diabetes, chronic respiratory 
disease, or cancer are more likely to develop serious illness. Anyone can get sick with COVID-19 and become 
seriously ill or die at any age.
</p>

        
<div>

<p float="centre">
    
<img src={prev} width="320" height="350" alt="" /> 
<img src={covidpeople} width="500" height="350" alt="" />
<img src={sym} width="430" height="350" alt="" /> 
</p>

<div>
         
        </div>
        
        </div>

        <h1 style={{ color: "green", fontFamily: "Kalam", fontWeight: 200,textAlign: 'center',fontSize: 40  }}><RiSurgicalMaskLine /> Covid Prevention</h1>
             <h3 style={{ color: "crimson", fontFamily: "Kalam", fontWeight: 200,textAlign: 'centre',fontSize: 22  }}>
             <b>To prevent infection and to slow transmission of COVID-19, do the following: </b>
             </h3>
             <ul style={{ color: "brown", fontFamily: "Kalam", fontWeight: 200,textAlign: 'centre',fontSize: 22  }}>
              <li>Stay at least 1 metre apart from others, even if they don’t appear to be sick.</li>
              <li>Wear a properly fitted mask when physical distancing is not possible or when in poorly ventilated settings.</li>
              <li>Choose open, well-ventilated spaces over closed ones. Open a window if indoors.</li>
                <li>Get vaccinated when a vaccine is available to you.</li>
                <li>Cover your mouth and nose when coughing or sneezing.</li>
                <li>If you feel unwell, stay home and self-isolate until you recover.</li>
         </ul>
<h1></h1>



            <h1> </h1>

            <h1 style={{ color: "green", fontFamily: "Kalam", fontWeight: 200,textAlign: 'center',fontSize: 40  }}> <FaExclamationTriangle /> Covid Symptoms</h1>
            <h3 style={{ color: "crimson", fontFamily: "Kalam", fontWeight: 200,textAlign: 'centre',fontSize: 22  }}>
             <b> COVID-19 affects different people in different ways. Most infected people will develop mild to moderate illness and recover without hospitalization.</b></h3>

            <ul style={{ color: "brown", fontFamily: "Kalam", fontWeight: 200,textAlign: 'centre',fontSize: 22  }}>
              <li>fever</li>
              <li>cough</li>
              <li>tiredness</li>
                <li>loss of taste and smell</li>
                <li>difficulty breathing or shortness of breath</li>
                <li>loss of speech or mobility, or confusion</li>
         </ul>
         <h3 style={{ color: "crimson", fontFamily: "Kalam", fontWeight: 200,textAlign: 'centre',fontSize: 22  }}>
             <b> Seek immediate medical attention if you have serious symptoms.  Always call before visiting your doctor or health facility. </b></h3>
             <h3 style={{ color: "crimson", fontFamily: "Kalam", fontWeight: 200,textAlign: 'centre',fontSize: 22  }}>
             <b> On average it takes 7-14 days from when someone is infected with the virus for symptoms to show. </b></h3>
             
        </div>
    )
}

export default GroupHome