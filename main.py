from fact import fact
import streamlit as st

def main():
    st.title('Factorial Calculator')
    n = st.number_input('Enter a number:', min_value=0)
    if st.button('Calculate'):
        try:
            st.write(f'The factorial of {n} is {fact(n)}')
            st.balloons()
        except:
            st.write('The number is too large to calculate the factorial. Please try a smaller number.')
if __name__ == '__main__':
    main()