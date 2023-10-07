import { useState } from 'react'

function MyButton() {
    const [count, setCount] = useState(1)
    function handleClick(){
        setCount(count + 1)
        alert(`You CLICKED me ${count} times!?! WHYYYY`)
    }
    return (
        <button onClick={handleClick}
            style= {{
                'backgroundColor': 'blue',
                'color':'white'
            }}
        >I'm a button! Click me!</button>
    )
}

export default MyButton