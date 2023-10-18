import Header from './components/Header'

function App() {
  const name = 'Brad'
  return (
    <div className="container">
      <Header title={'One'}/>
      <h1>Hello from React!</h1>
      <h2>Hello {name}! </h2>
    </div>
  );
}

export default App;
