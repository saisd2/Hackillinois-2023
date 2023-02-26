import React, { useEffect } from "react";
import ReactDOM from "react-dom";
import { Formik, Form, useField, useFormikContext } from "formik";
import * as Yup from "yup";
import styled from "@emotion/styled";
import "./styles.css";
import "./styles-custom.css";

const MyTextInput = ({ label, ...props }) => {
  // useField() returns [formik.getFieldProps(), formik.getFieldMeta()]
  // which we can spread on <input> and alse replace ErrorMessage entirely.
  const [field, meta] = useField(props);
  return (
    <>
      <label htmlFor={props.id || props.name}>{label}</label>
      <input className="text-input" {...field} {...props} />
      {meta.touched && meta.error ? (
        <div className="error">{meta.error}</div>
      ) : null}
    </>
  );
};

const MyCheckbox = ({ children, ...props }) => {
  const [field, meta] = useField({ ...props, type: "checkbox" });
  return (
    <>
      <label className="checkbox">
        <input {...field} {...props} type="checkbox" />
        {children}
      </label>
      {meta.touched && meta.error ? (
        <div className="error">{meta.error}</div>
      ) : null}
    </>
  );
};

// Styled components ....
const StyledSelect = styled.select`
  color: var(--blue);
`;

const StyledErrorMessage = styled.div`
  font-size: 12px;
  color: var(--red-600);
  width: 400px;
  margin-top: 0.25rem;
  &:before {
    content: "❌ ";
    font-size: 10px;
  }
  @media (prefers-color-scheme: dark) {
    color: var(--red-300);
  }
`;

const StyledLabel = styled.label`
  margin-top: 1rem;
`;

const MySelect = ({ label, ...props }) => {
  // useField() returns [formik.getFieldProps(), formik.getFieldMeta()]
  // which we can spread on <input> and alse replace ErrorMessage entirely.
  const [field, meta] = useField(props);
  return (
    <>
      <StyledLabel htmlFor={props.id || props.name}>{label}</StyledLabel>
      <StyledSelect {...field} {...props} />
      {meta.touched && meta.error ? (
        <StyledErrorMessage>{meta.error}</StyledErrorMessage>
      ) : null}
    </>
  );
};

// And now we can use these
const SignupForm = () => {
  return (
    <>
      <h1>Welcome Organization!</h1>
      <Formik
        initialValues={{
          company: "",
          amount: "",
          email: "",
          acceptedTerms: false,
        }}
//         validationSchema={Yup.object({
//           fullName: Yup.string()
//             .max(30, "Must be 30 characters or less")
//             .required("Required"),
//           amount: Yup.number()
//             .max(15, "Must be 15 characters or less")
//             .required("Required"),
//           email: Yup.string()
//             .email("Invalid email addresss`")
//             .required("Required"),
//           acceptedTerms: Yup.boolean()
//             .required("Required")
//             .oneOf([true], "You must confirm the transaction."),
//         })}
        onSubmit={async (values) => {
            alert(JSON.stringify(values));
            const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(values)
            };
        fetch('http://127.0.0.1:5000/check_suspicious', requestOptions).then((response) => response.json()).then((data) => {
                console.log(data);
                const obj = JSON.parse(JSON.stringify(data));
                if (obj.suspicious == "true") {
                    alert("This transaction has been flagged as a potential fraud, please review the transaction and speak with an associate for further details.")
                }
                else {
                    alert("This transaction has been verified, but please review transaction details before finalizing.");
                }
                if (obj.score >= 90) {
                    alert("Customer Score: This entity has a strong track record for payments and is unlikely to be unable to pay or commit fraud.");
                } else if (obj.score >= 70) {
                    alert("Customer Score: This entity has made most of their payments but might have missed a payment on occasion, careful in taking risks but fraud is unlikely");
                } else {
                    alert("Customer Score: We have detected this entity as a high risk, take caution in future transactions as they may be likely to fail payments or create fraud.");
                }
            })
        }}
      >
        <Form>
          <MyTextInput
            label="Customer"
            name="company"
            type="text"
            placeholder="Jane Doe"
          />
          <MyTextInput
            label="Transaction Amount"
            name="amount"
            type="text"
            placeholder="0.00"
          />
          <MyTextInput
            label="Email Address"
            name="email"
            type="email"
            placeholder="janedoe@example.com"
          />
          <MyCheckbox name="acceptedTerms">
            I confirm the following transaction
          </MyCheckbox>

          <button type="submit">Submit</button>
        </Form>
      </Formik>
    </>
  );
};

function App() {
  return <SignupForm />;
}

const rootElement = document.getElementById("root");
ReactDOM.render(<App />, rootElement);
