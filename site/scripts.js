function playNotes(f1, f2) {
    var context = new AudioContext();

    var oscillator1 = context.createOscillator();
    oscillator1.type = 'sine';
    oscillator1.frequency.value = f1;

    var oscillator2 = context.createOscillator();
    oscillator2.type = 'sine';
    oscillator2.frequency.value = f2;

    var gainNode = context.createGain();
    gainNode.gain.value = 0.5;

    oscillator1.connect(gainNode);
    oscillator2.connect(gainNode);
    gainNode.connect(context.destination);

    oscillator1.start();
    oscillator2.start();
    oscillator1.stop(context.currentTime + 1);
    oscillator2.stop(context.currentTime + 1);
}

function playNotesFromInputs() {
    var f1 = document.getElementById("first").value;
    var f2 = document.getElementById("second").value;
    playNotes(f1, f2);
}

function playNote(freq) {
			var context = new AudioContext();
			var oscillator = context.createOscillator();
			oscillator.type = 'sine';
			oscillator.frequency.value = freq;
			oscillator.connect(context.destination);
			oscillator.start();
			oscillator.stop(context.currentTime + 1);
		}