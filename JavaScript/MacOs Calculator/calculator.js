const display = document.getElementById('display');
let currentInput = '0';
let operator = null;
let previousInput = null;

document.querySelectorAll('.calc-button').forEach(button => {
    button.addEventListener('click', () => {
        const buttonId = button.id;

        switch (buttonId) {
            case 'clear':
                currentInput = '0';
                operator = null;
                previousInput = null;
                break;
            case 'plus-minus':
                currentInput = currentInput.startsWith('-') ? currentInput.slice(1) : `-${currentInput}`;
                break;
            case 'percentage':
                currentInput = (parseFloat(currentInput) / 100).toString();
                break;
            case 'divide':
            case 'multiply':
            case 'minus':
            case 'add':
                if (operator !== null) calculate();
                operator = buttonId;
                previousInput = currentInput;
                currentInput = '0';
                break;
            case 'equals':
                if (operator !== null) calculate();
                operator = null;
                previousInput = null;
                break;
            case 'decimal':
                if (!currentInput.includes('.')) currentInput += '.';
                break;
            default:
                if (currentInput === '0') {
                    currentInput = button.textContent;
                } else {
                    currentInput += button.textContent;
                }
                break;
        }

        display.textContent = currentInput;
    });
});

function calculate() {
    const prev = parseFloat(previousInput);
    const curr = parseFloat(currentInput);

    switch (operator) {
        case 'add':
            currentInput = (prev + curr).toString();
            break;
        case 'minus':
            currentInput = (prev - curr).toString();
            break;
        case 'multiply':
            currentInput = (prev * curr).toString();
            break;
        case 'divide':
            currentInput = (prev / curr).toString();
            break;
    }
}