import React from 'react'
import { Tooltip, XAxis, YAxis, ResponsiveContainer,LineChart,Line, BarChart, Bar,CartesianGrid, Legend } from 'recharts'
export function Graph1(props) {
    const info = [
    {
        name:"SSC",
        marks:90,
        
    },
    {
        name:"HSC",
        marks:85,
    },
    
]
    const info2 = [
        {
            sub:"Physics",
            SSC:95,
            HSC:80,

        },
        {
            sub:"Chemistry",
            SSC:88,
            HSC:80,

        },
        
        {
            sub:"Maths",
            SSC:98,
            HSC:91,

        },
        {
            sub:"English",
            SSC:89,
            HSC:85,

        },
        {
            sub:"Marathi",
            SSC:55,
            HSC:40,

        },
        {
            sub:"Hindi",
            SSC:70,
            HSC:72,

        },
    ]
    const getPath = (x, y, width, height) => (
        `M${x},${y + height}
         C${x + width / 3},${y + height} ${x + width / 2},${y + height / 3} ${x + width / 2}, ${y}
         C${x + width / 2},${y + height / 3} ${x + 2 * width / 3},${y + height} ${x + width}, ${y + height}
         Z`
      );
    const TriangleBar = (props) => {
        const {
          fill, x, y, width, height,
        } = props;
      
        return <path d={getPath(x, y, width, height)} stroke="black" fill={fill} />;
      };
      
    return (
        <>
          <ResponsiveContainer  width="50%" aspect={2}>
              <LineChart width = {50} height = {40} data = {info2} >
                <CartesianGrid strokeDasharray="5 5" />
                  <XAxis interval ={"preserveStartEnd"} dataKey="sub" stroke = "black" />
                  <YAxis tickFormatter = {(val)=>val+"%"} stroke = "black"/>

                  <Tooltip contentStyle = {{backgroundColor:"white"}}/> 
                  <Line type="monotone" stroke = "#8884d8" dataKey = "SSC"/> 
                  <Line type="monotone" stroke = "blue" dataKey = "HSC"/> 

                  </LineChart>

                  
          </ResponsiveContainer>
        <p><br></br></p>
          <ResponsiveContainer  width="50%" aspect={2}>
              <BarChart width = {50} height = {40} data = {info} barCategoryGap={80} >
              <CartesianGrid strokeDasharray="5 5" />
                  <XAxis interval ={"preserveStartEnd"} dataKey="name" stroke = "black"/>
                  <YAxis tickFormatter={(val)=>val+"%"} stroke = "black"/>

                  <Tooltip contentStyle = {{backgroundColor:"white"}}/> 
                  <Legend width={100} wrapperStyle={{ top: 40, right: 20, backgroundColor: '#f5f5f5', border: '1px solid #d5d5d5', borderRadius: 3, lineHeight: '40px' }} />
                  <Bar type="monotone" dataKey = "marks" fill = "#8884d8" strokeWidth={1}
                  shape={<TriangleBar/>}/> 
                  </BarChart>
          </ResponsiveContainer>
        </>
    )
}