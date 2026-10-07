import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

class NetworkAnomalyDetector:
    def __init__(self):
        # Isolation Forest is excellent for unsupervised anomaly detection
        self.model = IsolationForest(contamination=0.1, random_state=42)
        self.feature_names = ["Packet_Size_Bytes", "Request_Rate_Per_Sec", "Connection_Duration_Sec"]

    def generate_simulated_traffic(self, num_samples=200):
        """Generates baseline normal network traffic with some hidden malicious anomalies."""
        print("\n[System] Simulating live network traffic data stream...")
        np.random.seed(42)
        
        # 1. Normal Production Traffic (Moderate volume, typical packet sizes)
        # Parameters: [Mean Packet Size (~500B), Mean Request Rate (~50 req/s), Mean Duration (~5s)]
        normal_traffic = np.random.normal(loc=[500, 50, 5], scale=[50, 10, 1], size=(int(num_samples * 0.9), 3))
        
        # 2. Anomaly Type A: DDoS Attack Simulation (Massive rate, tiny packet sizes)
        # Parameters: [Low Packet Size (~40B), Huge Request Rate (~900 req/s), Tiny Duration (~0.5s)]
        ddos_attack = np.random.normal(loc=[40, 900, 0.5], scale=[5, 50, 0.1], size=(int(num_samples * 0.05), 3))
        
        # 3. Anomaly Type B: Data Exfiltration (Massive packet sizes, low rate, long duration)
        # Parameters: [Huge Packet Size (~5000B), Low Request Rate (~2 req/s), Long Duration (~120s)]
        exfil_attack = np.random.normal(loc=[5000, 2, 120], scale=[500, 0.5, 20], size=(int(num_samples * 0.05), 3))
        
        # Combine datasets
        raw_data = np.vstack([normal_traffic, ddos_attack, exfil_attack])
        np.random.shuffle(raw_data)
        
        df = pd.DataFrame(raw_data, columns=self.feature_names)
        # Ensure values stay realistic and positive
        return df.clip(lower=0.1)

    def train_and_detect(self, df):
        """Trains the ML model on the traffic matrix and flags structural anomalies."""
        print("[Engine] Fitting Isolation Forest model to traffic metrics...")
        
        # Separate configuration features from evaluation results
        features = df[self.feature_names]
        
        # Fit model and predict (-1 for anomaly, 1 for normal)
        self.model.fit(features)
        predictions = self.model.predict(features)
        
        df['Anomaly_Status'] = np.where(predictions == -1, 'Malicious/Anomaly', 'Normal')
        return df

    def visualize_threats(self, df):
        """Generates a 2D security analysis scatter plot highlighting classified attacks."""
        print("📊 Launching Threat Visualization System... Close window to return to menu.")
        
        plt.figure(figsize=(10, 6))
        
        # Separate data for plotting visual layers
        normal = df[df['Anomaly_Status'] == 'Normal']
        anomalies = df[df['Anomaly_Status'] == 'Malicious/Anomaly']
        
        plt.scatter(normal['Request_Rate_Per_Sec'], normal['Packet_Size_Bytes'], 
                    c='#2ca02c', label='Normal Traffic', alpha=0.6, edgecolors='k', s=50)
        
        plt.scatter(anomalies['Request_Rate_Per_Sec'], anomalies['Packet_Size_Bytes'], 
                    c='#d62728', label='Detected Security Threat', alpha=0.9, edgecolors='k', s=100, marker='X')
        
        plt.title("Cybersecurity Analytics: Network Traffic Anomaly Detection via ML", fontsize=12, fontweight='bold')
        plt.xlabel("Request Rate (Requests / Second)")
        plt.ylabel("Packet Size (Bytes)")
        plt.yscale('log') # Added logarithmic scaling to handle large differences in exfiltration vs normal packets
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.legend(loc='upper right')
        
        plt.tight_layout()
        plt.show()

def main():
    detector = NetworkAnomalyDetector()
    raw_traffic = None
    processed_traffic = None
    
    while True:
        print("\n" + "="*45)
        print("  AI-POWERED NETWORK SECURITY ANOMALY DETECTOR ")
        print("="*45)
        print("1. Simulate Network Traffic Data")
        print("2. Run Machine Learning Detection Engine")
        print("3. Plot Security Threat Matrix")
        print("4. Exit Engine")
        
        choice = input("Select operation (1-4): ").strip()
        
        if choice == "1":
            raw_traffic = detector.generate_simulated_traffic()
            print(f"✔️ Successfully captured {len(raw_traffic)} network traffic blocks.\n")
            print(raw_traffic.head(10).to_string(index=False))
            print("\n... [Truncated for preview] ...")
        
        elif choice == "2":
            if raw_traffic is None:
                print("❌ Error: Please simulate traffic data first (Option 1).")
            else:
                processed_traffic = detector.train_and_detect(raw_traffic)
                anomaly_count = len(processed_traffic[processed_traffic['Anomaly_Status'] == 'Malicious/Anomaly'])
                print(f"\n⚡ Scan Complete! Identified {anomaly_count} potential malicious packets.")
                print(processed_traffic[['Packet_Size_Bytes', 'Request_Rate_Per_Sec', 'Anomaly_Status']].head(15))
                
        elif choice == "3":
            if processed_traffic is None:
                print("❌ Error: Run the detection engine first (Option 2) before plotting.")
            else:
                detector.visualize_threats(processed_traffic)
                
        elif choice == "4":
            print("[System] Terminating security matrix. Goodbye!")
            break
        else:
            print("❌ Invalid command option.")

if __name__ == "__main__":
    main()