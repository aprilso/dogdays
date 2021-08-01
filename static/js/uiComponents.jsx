//MELON example code

// function Homepage(props) {
//   return (
//     <div id="home-banner" className="row">
//       <div className="col">
//         <h1>Ubermelon</h1>
//         <p className="lead">Melons on demand.</p>
//       </div>
//     </div>
//   );
// }


// function Navbar(props) {
//   const { logo, brand } = props;

//   return (
//     <nav>
//       <ReactRouterDOM.Link
//         to="/"
//         className="havbar-brand d-flex justify-content-center"
//       >
//         <img src={logo} height="30" />
//         <span>{brand}</span>
//       </ReactRouterDOM.Link>

//       <section className="d-flex justify-content-center">
//         <ReactRouterDOM.NavLink
//           to="/shop"
//           activeClassName="navlink-active"
//           className="nav-link nav-item"
//         >
//           Shop for Melons
//         </ReactRouterDOM.NavLink>
//         <ReactRouterDOM.NavLink
//           to="/cart"
//           activeClassName="navlink-active"
//           className="nav-link nav-item"
//         >
//           Shopping Cart
//         </ReactRouterDOM.NavLink>
//       </section>
//     </nav>
//   );
// }