import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
function MyButton() {
  return (
    <button>I'm a button</button>
  );
}
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          To Infinity And Biond
        </a>
        <MyButton/>
      </header>
      <body></body>
    </div>
  );
}
export default App;
