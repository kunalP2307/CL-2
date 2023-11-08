from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute, IBMQ

IBMQ.enable_account('0b456d213ef175d138eec5819bd9c7e0e5632794df655bb6673ac4d4466eaa512e80b7d747728a8bed03209cf11221bce342256ec3f5a3b0cf6fce04cfd1ee9a')
provider = IBMQ.get_provider(hub='ibm-q')

q = QuantumRegister(16, 'q')
c = ClassicalRegister(16, 'c')
circuit = QuantumCircuit(q, c)
circuit.h(q)
circuit.measure(q, c)

backend = provider.get_backend('ibmq_qasm_simulator')
job = execute(circuit, backend, shots=1)

print('Executing Job...\n')
result = job.result()
counts = result.get_counts(circuit)

print('RESULT: ', counts, '\n')
print('Press any key to close')
circuit.draw()
input()
